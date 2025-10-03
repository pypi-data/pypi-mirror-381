# dockreg - Private Docker Registry Manager

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

## Installation and Usage

See [Dockreg on GitHub](https://github.com/jin-gizmo/dockreg).
