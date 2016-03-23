Install docker command line tools: https://www.docker.com/products/docker-toolbox
Install git command line tools: https://git-scm.com/download/mac
Clone repo and cd into it on your local machine

1. Create local virtual machine named clicc

```
docker-machine create -d virtualbox clicc
```

2. Point docker daemon to virtual machine

```
docker-machine env clicc
```

3. Follow instructions to set docker daemon env

```
eval $(docker-machine env)
```

4. Run docker compose to orchestrate container build

```
docker-compose up -d
```

5. Save dynamic ip address of local virtual machine

```
DOCKER_IP=$(docker-machine ip clicc)
```

6. Open interactive session within a docker container hosted database (password: clicc)

```
psql -U clicc -W -h $DOCKER_IP
```
