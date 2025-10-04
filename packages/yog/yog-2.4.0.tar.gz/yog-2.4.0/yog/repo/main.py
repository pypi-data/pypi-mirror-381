import logging
import os
import subprocess
import typing as t
import re
from argparse import ArgumentParser
import json

import yaml
from docker.models.images import Image

from yog.git_utils import require_clean_work_tree
from subprocess import check_output
import docker
from dataclasses import dataclass

from yog.logging_utils import setup
from yog.ssh_utils import ScopedProxiedRemoteSSHTunnel

log = logging.getLogger(__name__)


@dataclass
class PushTarget:
    dockerfile_path: str
    registry_url: str = None
    tunnel_host: str = None
    tunnel_port: int = 5000
    context_path: str = None
    tags: t.List[str] = None
    repository: str = None

    def validate(self):
        if not self.is_private_registry() and not bool(self.tags):
            raise ValueError("You need to specify explicit tags to push if you're pushing to docker hub.")

    def is_private_registry(self):
        return bool(self.registry_url)


def _load_targets() -> t.Dict[str, PushTarget]:
    with open("./yog-repo.conf", "r") as fin:
        obj = yaml.full_load(fin)
    targets = {target_name: PushTarget(**target_dict) for target_name, target_dict in obj.items()}
    return targets

def ls():
    log.info("Available targets:")
    target: PushTarget
    for tname, target in _load_targets().items():
        log.info(f"{tname}: {target.registry_url}/{target.repository}")

def push(target: str, check_unclean_work_tree: bool):
    targets = _load_targets()

    push_target: PushTarget = targets[target]

    push_target.validate()

    if push_target.context_path:
        os.chdir(push_target.context_path)

    if check_unclean_work_tree and not require_clean_work_tree():
        raise RuntimeError("Your work tree is not clean.")

    revision = check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

    if push_target.tunnel_host:
        log.info(f"Establishing tunnel to {push_target.tunnel_host}:{push_target.tunnel_port}")
        tunnel = ScopedProxiedRemoteSSHTunnel(push_target.tunnel_host, push_target.tunnel_port)
        tunnel_port = tunnel.connect()
    else:
        tunnel = None
        tunnel_port = None

    try:
        if push_target.tunnel_host:
            tag = f"localhost:{tunnel_port}/{push_target.repository}:{revision}"
        elif push_target.registry_url:
            tag = f"{push_target.registry_url}/{push_target.repository}:{revision}"
        else:
            tag = f"{push_target.repository}:{revision}"
        log.info(f"tag: {tag}")

        client: docker.DockerClient = docker.DockerClient(base_url='unix://var/run/docker.sock')
        log.info(f"Dockerfile: {push_target.dockerfile_path}")

        labels: t.Dict[str, str] = dict()
        labels["cafe.josh.yog.git-head-sha"] = revision

        log.info("Building...")
        image: Image
        image, logs = client.images.build(path=".", dockerfile=push_target.dockerfile_path, rm=True, tag=tag, labels=labels)

        log.info("Tagging...")
        if push_target.tags:
            for extra_tag in push_target.tags:
                image.tag(push_target.repository, extra_tag)

        log.info("Pushing...")
        if push_target.is_private_registry():
            subprocess.check_call(["docker", "push", tag])
        else:
            subprocess.check_call(["docker", "push", tag, "--all-tags"])
        log.info("Done.")

    finally:
        if tunnel:
            tunnel.disconnect()


def main():
    setup("yog")
    args = ArgumentParser()

    args.add_argument("--workdir", default=None)

    subparsers = args.add_subparsers(help="Subcommand arguments.", dest="subcommand")
    push_parser = subparsers.add_parser("push")
    push_parser.add_argument("target")
    push_parser.add_argument("--no-git-check", action="store_true")

    list_parser = subparsers.add_parser("ls")

    prune_parser = subparsers.add_parser("prune")

    opts = args.parse_args()
    log.debug(f"Invoked with: {opts}")

    if opts.workdir:
        log.info(f"chdir: {opts.workdir}")
        os.chdir(opts.workdir)

    if opts.subcommand == "push":
        push(opts.target, not opts.no_git_check)
    elif opts.subcommand == "ls":
        ls()
    else:
        log.error(f"Invalid command: {opts.subcommand}")





