# Overview

An opinionated docker-and-ssh-centric declarative system management tool.

`pip3 install yog`

Features:

* Like puppet or ansible but a lot smaller and focused on docker, files, and cron
* agentless - runs entirely on top of ssh
* entirely defers auth(z/n) to ssh and the remote system's user permissions

Non-features:

* No intentional ipv6 support. I don't have anything against IPv6, but my ISP doesn't give me a v6 address and as such I
  don't run ipv6 on my lan. So since I can't test it at all, I just kind of disregard it, especially where it lets me
  make the ipv4 UX better.

Command summary:

* `yog`: Applies configurations to hosts. e.g. `yog myhost.mytld` applies the config from `./domains/mytld/myhost.yml`.
* `yog-repo`: Manages a docker repository. `yog-repo push` uses the contents of `./yog-repo.conf` to build an image and
  push it to the configured registry with the configured name and tag.

Example run:

[usage.webm](https://user-images.githubusercontent.com/1287152/209723654-e78b5283-60b5-4894-b5a1-3d2d71bfcc45.webm)

# Setup

1. Configure docker to listen on localhost's port 4243 (which is the default). See below.
2. Use `ssh-copy-id` to copy your ssh key to all the servers you wish to manage. You can look into ssh certificates if
   you want a more general ssh PKI solution.
3. Configure the target system to allow you to use sudo without a password. [2]
4. That's it. You now serve the nameless mist. Do you hear whippoorwills?

## Docker port listening setup (step 1)

```bash
ssh myhost
sudo systemctl edit docker
```

And add `-H tcp://127.0.0.1:4243` to the command. So for me, that file looks like:

```text
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://127.0.0.1:4243
```

Yog will apply files before docker containers, so you might also want to add a yog file entry like so:

```yaml
files:
  - src: docker-override.conf
    dest: /etc/systemd/system/docker.service.d/override.conf
    root: yes
    hupcmd: sudo systemctl restart docker
```

# Usage

Yog uses YML files that it calls "necronomicons" for configuration of hosts. It's organized hierarchically so
that a necronomicon for "mytld" will be applied to all hosts under that TLD.

Let's learn by example:

Suppose we have a folder, that can be named whatever we want, at `~/projects/my-config`. This is the root of a
git repo, and is also the root of our yog configuration. Make this your current working dir, or pass `--root-dir`.

`$ cd ~/projects/my-config`

```text
.
├── domains
│      ├── com
│      │      └── example
│      │          └── myhost.yml
│      └── com.yml
└── files
    ├── example.txt
    ├── hello_world.html
    └── helloworld-nginx.conf

4 directories, 5 files
```

Files that can be sent to hosts are stored under `files`.

Host configurations - necronomicons - are stored under `domains`.

If we want to apply `myhost.yml`, we run:

`yog myhost.example.com`

Example output:

```text
$ yog myhost.example.com
[2022-12-26 11:01:52,514] [INFO]: [myhost.example.com]
[2022-12-26 11:01:59,121] [INFO]: [myhost.example.com][files]: OK [hello_world.html]
[2022-12-26 11:01:59,274] [INFO]: [myhost.example.com][files]: OK [helloworld-nginx.conf]
[2022-12-26 11:02:07,117] [INFO]: [myhost.example.com][docker]: OK registry@sha256:8be26f81ffea54106bae012c6f349df70f4d5e7e2ec01b143c46e2c03b9e551d
```

## Necronomicon format

Let's look at a necronomicon.

```yml
files:
  - src: hello_world.html
    dest: /srv/hello_world/hello_world.html
    root: yes
  - src: helloworld-nginx.conf
    dest: /etc/nginx/conf.d/helloworld.conf
    root: yes
    hupcmd: sudo systemctl restart nginx


docker:
  - image: registry
    name: my-registry
    fingerprint: sha256:8be26f81ffea54106bae012c6f349df70f4d5e7e2ec01b143c46e2c03b9e551d
    volumes:
      images: /var/lib/registry
    ports:
      - container: 5000
        host: [ 5000 ]
    env:
      REGISTRY_STORAGE_DELETE_ENABLED: true

pki:
  certs:
    - authority: my-ca
      storage: /srv/pki/myhost/
      validity_years: 2
      refresh_at: 1
      names:
        - myhost.local
        - myapp.local
```

### Files

Files are checked for equality via hash-comparison. I've found this a useful way to manage:

* cron files in /etc/cron.d/
* Root certificates to put in the system trust store[1]
* random config files

Attributes:

* `src`: the source. This is a _relative_ path rooted at the `files` directory in the hierarchy. You can use
  intermediate dirs.
* `dest`: the destination filepath on the managed host. This is an absolute path.
* `root`: whether to `sudo` to root for the file put. This mainly picks who owns the file + can access files, but this
  might have other useful properties for your use case. If set to `no`, the put operation is run as your ssh user.
* `hupcmd`: a command to run after the file is placed. A common thing in ye olde days was to send SIGHUP to a process
  which would handle it by reloading the config. Commonly nowadays you might be
  using `hupcmd: sudo systemctl reload nginx`

### Docker containers

Docker containers are compared on all specified attributes and won't unnecessarily restart containers.

Attributes:

* `image`: the docker repository name. e.g. `itzg/minecraft-server` or `dockerrepo.local:5000/mything`
* `name`: the container name.
* `fingerprint`: sha digest of the desired version. Tags are bad news bears so we don't support them. This is called
  fingerprint instead of digest because I didn't know they were called digests when I first coded this and then never
  changed it once I did.
* `volumes`: volumes to attach. see below.
* `ports`: ports to open. see below.
* `env`: environment variables to set.

#### Volumes

For volumes, the key is the volume name and the value is the mount point.

For bind mounts, the key is the host path and the value is the container path.

#### Ports

It's a list of:

```text
container: port/protocol
host: [interface_ip:port, interface_ip:port]
```

For the container, you can omit the protocol to get tcp by default.

For the host, you can omit the interface ip to get `0.0.0.0` which binds all interfaces.

Examples:

```yml
- container: 53/tcp
  host: [ 192.168.1.103:53, 127.0.0.1:53 ]
- container: 53/udp
  host: [ 192.168.1.103:53, 127.0.0.1:53 ]
- container: 33200 # tcp is implicit default, this is the same behavior as docker
  host: [ 33200 ] # binds 0.0.0.0
- container: 3000
  host: [ 8080 ]
```

### Public Key Infrastructure (PKI)

Yog supports low-fuss local/private PKI management.

You'll define certificate authories in `cas.yml` which is in your yog root (so, right next to `domains` and `files`).

Example `cas.yml`:

```yaml
- ident: my-ca
  storage: "myhost.local:/srv/yog/ca/my-ca/"
  validity_years: 3
```

As you can see, yog tries to keep you out of the crypto weeds.

`ident` is both how you'll refer to this CA in necronomicons, and also the X.509 Common Name.
`storage` is a string of format `<host>:<path>` where the trust material will be stored. More on that below.
`validity_years` is how long the cert will be valid for upon generation.

Once you've defined `cas.yml`, you can run `yog-pki`.

```text
$ yog-pki
Generating new CA...
```

Now you can use it in necronomicons.

```yaml
pki:
  certs:
    - authority: my-ca # this has to refer to an "ident" in cas.yml
      storage: /srv/pki/myhost/
      validity_years: 2
      refresh_at: 1 # yog runs will only renew a cert once the remaining validity time is < this number of years
      names:
        - myhost.local # first entry becomes X.509 Common Name
        - myapp.local # subsequent names are X.509 Alternative Names
```

#### Trust Material Formats and Storage

When yog or yog-pki write trust material to disk, it will restrict read access for private material but allow it for
public.

Yog writes multiple formats to facilitate as many use-cases as possible with the same PKI:

| Filename             | Format              | Encoding | Public/Private | Notes                 |
|:---------------------|:--------------------|:---------|:--------------:|-----------------------|
| key.pem.openssl      | Traditional OpenSSL | PEM      |    private     | good for nginx        |
| key.ssh              | SSH                 | SSH      |    private     |                       |
| key.pem.pkcs1.public | PEM                 | PKCS1    |     public     | java's JCE likes this |
| key.ssh.public       | SSH                 | SSH      |     public     |                       |
| key.crt              | X.509 Certificate   | PEM      |     public     | good for nginx        |

#### Crypto Remarks

Yog tries to keep you out of the weeds and also to be a good, expressive, concise tool for what it considers itself good at.

You don't need to, and shouldn't want to, read this section. It is here to help reassure anyone who knows
too much about cryptography and wants to know some details.

Yog-pki uses Python's Rust-based cryptography module and doesn't do anything clever at all (which is dangerous in crypto).

It uses elliptic-curve keys, and uses the NIST P-384 R1 curve (known as `SECP384R1` in python's cryptography module).
This is a 384-bit key, roughly equivalent to the hardness of a 7000-bit RSA key. 

It uses CN and Alternative Names to set the "names" that certificates represent. 

Nothing else is configurable. Small tweaks come in the future but generally speaking,
I don't intend for yog-pki to handle huge, complicated PKIs. If you need to do so, 
you might want to look at https://smallstep.com/. (You can use Yog's docker and file capabilities to
deploy a smallstep installation!)

### `pipx` Package Management

```commandline
pipx:
  extra_indices:
    - https://myrepo.local/
  packages:
    - name: mypkg
      version: 1.0
```

# Footnotes

[1] This is one of those things where I feel like you probably shouldn't manage root certs like this but I have yet to
regret it? It's not a cryptographic secret, so.

[2] Also something that people say you probably shouldn't do but I've yet to regret. If your user is in the docker group
it's basically root anyway from a threat modeling perspective.

# `yog-repo`

Yog also includes a tool for pushing images to your local docker registry. I haven't documented it yet, apologies. 
