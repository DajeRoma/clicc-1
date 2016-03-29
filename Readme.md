# Containers 101

Linux containers are not new. They have been around for a long time. However, nearly all of the tools that are currently available for creating, managing, discovering, and running linux containers are new. And it is the relatively recent availability of this support tooling that has made linux containers really take off in terms of cloud based application deployment. 

You all part of a team that is building a complex, distributed web application. And, as such, you are going to have to learn more about how the modern web actually operates than the average Environmental Scientist in order to be successful with your work (even if you think that your personal role within the project has no outward facing components).

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/vm-vs-docker.png "Containers vs. Virtual Machines")

# The Docker Approach

Docker provides an integrated set of tools and services which enable you to take some code that you have developed alone, say in your office, on your personal laptop, and do one or more of the following:

- package that code and all its dependencies (all the 3rd party packages, the language runtime, the os, hell, the kitchen sink...everything) into an immutable form (called a container) such that you can GUARANTEE that it will always run, in the exact same way, basically forever, on anyone else's machine, anywhere in the world. 

- provide version control and web hosting services for your container (which you can probably imagine might still get quite large: >1 GB sometimes) in such a way that you can easily distribute it to anyone that you might want to share your code with (including yourself, perhaps in the future) anywhere.

- automate the transfer and unpackaging of that container both one your own machine or on a set of one or more super crazy powerful machines that you can rent in the cloud from Amazon, Google, etc.

- automate control of the network's access to your container from agents on the web such that your container can talk to other containers, living on other machines, in other clouds, or even to multiple replicated versions of itself (yes, this is possible, and about where things start to get interesting...)

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker_datacenter_toolchain.jpg "Docker Datacenter Toolchain and Services")

# The Docker Ecosystem

What has made Docker so successful thus far is its simplicity of use and the breadth and depth of its integrations. Docker lets you build an application stack based on any programming language, any database, and any operating system (as long as its linux), wrap them up in a container, and push them to any cloud. This flexibility goes a long way towards allowing you to: 

- be efficient with your time: no need to learn some new language to develop your app because its the one of the select few hosted by your cloud provider of choice

- be efficient with your money: choose the cloud provider that offers the set of services which is best suited to your needs for the least cost possible. If their terms or their prices change over time, no big deal, you can move your entire app to another cloud with trivial ease...

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker-ecosystem.jpg "Docker Ecosystem")

# The Docker Orchestration Tools

Docker provides its own set of orchestration tools that are tightly integrated with the Docker-Hub - a public/private registry where you can store your repositories and acess those belonging to others - as well as with the various partner services described previously as being part of the Docker ecosystem. The docker orchestration toolset's four key components are each described separately below.

## ````docker-machine````

Docker Machine allows developers to work with the Docker Engine from a local laptop, giving them the ability to prepare any Linux host to a data center VM, bare metal, or a remote cloud instance, and to run and manage Dockerized apps on all hosts (remote or local) all through a single interface. What's more, the backend API extends the Docker Machine to any infrastructure or service provider including: Amazaon, Google Cloud, Rackspace, DigitalOcean, Cloudfoundry, etc., etc., ...

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker-machine.png "Docker-Machine")

## ````docker-compose````

Docker Compose allows developers to define which set of Docker containers should comprise the multi-container distributed application. It allows you to dynamically change the application and add new services as needed.

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker-compose.png "Docker-Compose")

## ````docker-swarm````

Docker Swarm offers native clustering capabilities for large-scale applications. It's able to automatically optimize for workload and placement based on resource utilization. Using standard and custom constraints, it enables complex placement optimization, and upon host failure, it's able to automatically rebalance workloads to provide HA and fault tolerance.

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker-swarm.png "Docker-Swarm")

## ````docker````

The Docker-Engine (or sometimes, Docker Daemon) controls the low level interface between the containers and their underlying hardware (the bare metal). This is the tool that allows you to collectively view and manage containers on a single host machine as well as interactively control containers (by attaching to them and running local shell commands from inside any given container).

# Working with the CLiCC Docker Containers

This repository contains the build instructions for a customized set of docker containers that are designed to act as the CLiCC development environment. The automated build configuration generates a linked set of three containers housed in a single virtual machine living on the user's local host system. Two of the three containers are for data storage (a persistent data store container linked to an ephemeral postGIS database container). The third container is bridged to the other two interally within the VM and is accessibly over the internet as an iPython notebook server. This server provides Python 2.7 and 3.3 development environments with a number of key scientific computing packages pre-installed. This allows you to build up codebases as iPython notebooks within the browser, but saved onto the hosting container. This will very closely simulate the experience of working with a cloud hosted virtual machine. A conceptual diagram of this system architecture is desribed in the image below.

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/dev-architecture.png "Development-Architecture")

## Building and running the CLiCC development environment

Install docker command line tools: https://www.docker.com/products/docker-toolbox

Install git command line tools: https://git-scm.com/download/mac

Clone this repo and cd into it on your local machine

1. Create local virtual machine named clicc

```
docker-machine create -d virtualbox clicc
```

2. Associated docker daemon with new virtual machine ip

```
docker-machine env clicc; eval $(docker-machine env clicc)
```

3. Run docker compose to orchestrate container builds

```
docker-compose up -d
```

4. Check to see that the containers are active

```
docker-compose ps
```

This command should show you some output like the following:

```
   Name                 Command               State            Ports
-----------------------------------------------------------------------------
clicc_data   /bin/true                        Exit 0
clicc_db     /docker-entrypoint.sh postgres   Up       0.0.0.0:5432->5432/tcp
clicc_dev    /initdev.sh                      Up       0.0.0.0:443->8888/tcp
```

4. Open interactive database session within the clicc_db_1 container hosted database (user:clicc, password: clicc)

```
psql -h $(docker-machine ip clicc) -p 5432 -d clicc -U clicc
```

This brings you to an interactive SQL session with the postGIS database container. You can test some queries or create a new datastore. To leave this session and return to the shell simply type in: "\q"

5. Open interactive ipython notebook session hosted on the clicc_dev_1 container (password:clicc)

```
docker-machine ip clicc
```

This command should show you the ip address that was dynamically generated for the clicc VM as in the following:

```
192.168.99.100
```

6. Open your browser (preferrably chrome) and type the following url =>  https://[YOUR VM'S IP]

Ignore any warnings that you may get from the browser about certificates and security. Our docker container running the ipython notebook server is not using a valid signed certificate. Those cost money that we don't have. Plus it is not something that we need for this development environment.

Input the password for the ipython notebook server (clicc) and voila!