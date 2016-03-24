# Containers 101

Linux containers are not new. They have been around for a long time. However, nearly all of the tools that are currently available for creating, managing, discovering, and running linux containers are new. And it is the relatively recent availability of this support tooling that has made linux containers really take off in terms of cloud based application deployment. 

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/vm-vs-docker.png "Containers vs. Virtual Machines")

Whether you know it or not, whether you like it or not, whether you care or not: you all part of a team that is building a complex, distributed web application. And, as such, you are going to have to learn more about how the modern web actually works than the average Environmental Scientist in order to be successful with your work (even if you think that your personal role within the project has no outward facing components).

# The Docker Approach

Docker provides an integrate set of tools and services which enable you to take some code that you have developed alone, say in your office, on your personal laptop and do the following:

- package that code and all its dependencies (all the 3rd party packages, the language runtime, the os, hell, the kitchen sink...everything) into an immutable form (called a container) such that you can GUARANTEE that it will always run, in the exact same way, basically forever, on anyone else's machine, anywhere in the world. 

- version control and provide web hosting services for your container (which you can probably imagine might still get quite large: >1 GB sometimes) in such a way that you can easily distribute it to anyone that you might want to share your code with (including yourself, perhaps in the future) anywhere.

- automate the unpackaging of that container and the management of its interaction with other containers living either on your own machine or on a set of one or more super crazy powerful machines that you can rent in the cloud from Amazon, Google, etc.

- automate control of the network's access to your container from agents on the web such that your container can talk to other containers or multiple versions of itself (yes, this is possible, and about where things start to get interesting...)

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker_datacenter_toolchain.jpg "Docker Datacenter Toolchain and Services")

# The Docker Ecosystem

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker-ecosystem.jpg "Docker Ecosystem")

# The Docker Orchestration Tools

Docker provides its own set of orchestration tools that are tightly integrated with the Docker-Hub - a public/private registry where you can store your repositories and acess those belonging to others - as well as with the various partner service described previously as being part of the Docker ecosystem.

The docker orchestration toolset' four key components are each described separately below.

## ````docker-machine````

Docker Machine allows developers to work with the Docker Engine from a local laptop, giving them the ability to prepare any Linux host to a data center VM, bare metal, or a remote cloud instance, and to run and manage Dockerized apps on all hosts (remote or local) all through a single interface. What's more, the backend API extends the Docker Machine to any infrastructure or service provider including: Amazaon, Google Cloud, Rackspace, DigitalOcean, Cloudfoundry, etc., etc., ...

## docker-compose

## docker-swarm

## docker-network

## docker





Install docker command line tools: https://www.docker.com/products/docker-toolbox

Install git command line tools: https://git-scm.com/download/mac
Clone repo and cd into it on your local machine

1. Create local virtual machine named clicc

```
docker-machine create -d virtualbox clicc
```

2. Point docker daemon to virtual machine

```
eval $(docker-machine env clicc)
```

3. Run docker compose to orchestrate container build

```
docker-compose up -d
```

4. Open interactive session within a docker container hosted database (password: clicc)

```
psql -U clicc -W -h $(docker-machine ip clicc)
```
