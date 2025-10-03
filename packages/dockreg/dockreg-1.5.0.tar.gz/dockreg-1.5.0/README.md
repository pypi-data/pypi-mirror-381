# dockreg - Private Docker Registry Manager

> [!NOTE]
> **About this project**
> 
> **Dockreg** was developed at [Origin Energy](https://www.originenergy.com.au)
> as part of the *Jindabyne* initiative. While not part of our core IP, it proved
> valuable internally, and we're sharing it in the hope it's useful to others.
> 
> Kudos to Origin for fostering a culture that empowers its people
> to build complex technology solutions in-house.
> 
> See more tools at [Jin Gizmo on GitHub](https://jin-gizmo.github.io).

## Overview

**Dockreg** is a simple utility for deploying and managing a private docker
registry running on the local machine in a docker container.

Why?

In a nutshell ... to support building multi-platform docker images and provide a
simple test rig when you don't want to push a not-quite-ready docker build to
somewhere more exposed.

## Capabilities

**Dockreg** can create and manage a fully functional docker registry, running in
a docker container with persistent storage in the local filesystem. All of the
normal docker commands (pull, push etc.) work as expected.

Dockreg provides a CLI with subcommands to:

* start and stop the registry
* view and delete registry contents
* copy docker images to AWS ECR or another docker registry.

## Installing Dockreg

### Prerequisites

**Dockreg** depends on docker to be able to run the standard docker [registry
image](https://hub.docker.com/_/registry). It has been tested with [Docker
Desktop](https://www.docker.com/products/docker-desktop/) on macOS.

### Install with Pip

```bash
pip install dockreg
```

### Installing from the Repo

Clone the repo, then:

```bash
cd dockreg
# Create a virtualenv, set up the work area. Idempotent
make init
source venv/bin/activate

# Get help
make

# Build the pip installable package into "dist" directory
make pkg
```

To run the code directly from the repo:

```bash
python3 -m dockreg.cli.dockreg --help
```

## Using Dockreg

### TL;DR

```bash
# Start a registry localhost:5001
dockreg start

# Tag a local image and push it to our private registry
docker tag my-image localhost:5001/my-image
docker push localhost:5001/my-image

# Check that it appears in our private registry
dockreg images

# Inspect the image in the private registry
dockreg inspect localhost:5001/my-image

# When done
dockreg stop
```
### Usage

```
usage: dockreg [-h] [-v] [-r REGISTRY] command [command-args]

Interact with a local docker registry.

Commands:
    cp (copy)           Copy an image from the local registry to another
                        docker registry.
    cpe (copy2ecr)      Copy an image from the local registry to AWS ECR.
    gc                  Garbage collect and restart the registry container.
    info (ps)           List registry containers and show their configuration.
    ins (inspect)       Inspect specified images.
    ls (repos)          List repositories in the registry.
    lsi (images)        List images in the specified repos.
    restart             Restart the registry container.
    rmi (delimage)      Delete specified images.
    rmr (delrepo)       Delete all images in the specified repositories.
    start (up)          Start a registry container.
    stat (status)       Get status of the registry container (exit status 0 if
                        running, 1 otherwise).
    stop (down)         Stop the registry container.

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -r REGISTRY, --registry REGISTRY
                        The source registry to use. Default is localhost:5001.
```

> Note that the *registry* docker image will use port 5000 by default. On macOS,
> port 5000 is used by a system service, hence the move to 5001 in **dockreg**.
> This can be changed using the `-r` / `--registry` option.

To get help on individual commands:

```bash
dockreg <CMD> --help
```

> Unless a different location is specified as an argument to the `start` command,
> **dockreg** will persist the registry in `~/.dockreg`. It's a good idea to
> exclude this directory from Time Machine backups.

## Multi-platform Docker Images

The conventional method for building docker images will produce an image for a
single platform, generally the one on which it was built. There are situations
where a docker image may need to be usable on different platforms, typically ARM
(`linux/arm64`) and x86 (`linux/amd64`). In this case, a multi-platform manifest
image is needed. For example, the various Linux base images are multi-platform.
A docker pull command will automatically get the image that matches the client
platform, unless instructed otherwise.

The process for building multi-platform images differs from the process of
building a single-platform image. A single platform image can be built, and then
pushed to a registry in two separate steps. A multi-platform image must be built
and pushed to a registry in a single step. **Dockreg** provides a suitable
private registry for this purpose during development and testing.

As an example, consider the following sample Dockerfile (`etc/Dockerfile.sample`
in the repo).

```dockerfile
FROM alpine:latest
ENTRYPOINT [ "/bin/arch" ]
```

The normal process for building the image would be:

```bash
cd etc
docker build -f Dockerfile.sample -t archy .
```

We can run a container from the image and get the obvious result (on M series
Mac in this case)

```bash
❯ docker run --rm archy
aarch64
```

The image will only run on the same hardware architecture used to create it.

We can push the image to our **dockreg** local registry:

```bash
# Start our local registry
dockreg start
# Tag and push our new image
docker tag archy localhost:5001/archy
docker push localhost:5001/archy
```

Inspecting the image shows that it supports only a single platform:

```
❯ dockreg inspect localhost:5001/archy

IMAGE                 TAG     PLATFORM     DIGEST
--------------------  ------  -----------  ----------------------------------
localhost:5001/archy  latest               sha256:dad7855fe36ce6f45d500a8f...
                              linux/arm64  sha256:e7b46d0976e5e48321abf416...
```

To build the image as a multi-platform image for x86 and ARM:

```bash
cd etc
docker buildx build --platform linux/amd64,linux/arm64 -f Dockerfile.sample \
    -t localhost:5001/archy --push .
```

Key points:

1.  We have switched to using [buildx](https://docs.docker.com/reference/cli/docker/buildx/)
    for the build.
2.  Target platforms are explicitly requested: `--platform linux/amd64,linux/arm64`
3.  The image *must* be tagged and pushed as part of the process:
    `-t localhost:5001/archy --push`

Inspecting the image now shows that it supports both platforms:

```
❯ dockreg inspect localhost:5001/archy

IMAGE                 TAG     PLATFORM     DIGEST
--------------------  ------  -----------  ----------------------------------
localhost:5001/archy  latest               sha256:ee28f8bb62a5a0c059f3570c...
                              linux/amd64  sha256:44f1a59d4c4de8d0d4e01cc7...
                              linux/arm64  sha256:4018600f0bcc32aaa506a595...
```

We can run both versions of the our image (using emulation for x86 on M series
Mac):

```
# This will pick the image that matches the host platform
❯ docker run --rm localhost:5001/archy
aarch64

# Explicitly request an ARM version
❯ docker run --rm --platform linux/arm64 localhost:5001/archy
aarch64

Explicitly request an x86 version
❯ docker run --rm --platform linux/amd64 localhost:5001/archy
x86_64
```

## Docker Configuration on macOS

These are the suggested settings in [Docker
Desktop](https://www.docker.com/products/docker-desktop/) on macOS to support
multi-platform builds.

![](doc/img/docker-config.png)

## Release Notes

#### v1.5.0

*   Added description to help messages for subcommands.

#### v1.4.0

*   Open source base release.
