# Containers 101

![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/vm-vs-docker.png "Containers vs. Virtual Machines")

# The Docker Toolchain
![alt text](https://github.com/ericdfournier/clicc/blob/master/src/common/images/docker_datacenter_toolchain.jpg "Docker Datacenter Toolchain and Services")


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
