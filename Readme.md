1. Pull image repository from docker hub.

```
docker pull ericdfournier/clicc_db:latest
```

2. Run docker image with new user and new password for clicc

```
docker run -p 5432:5432 -e POSTGRES_USER=clicc -e POSTGRES_PASSWORD=clicc ericdfournier/clicc_db
```

3. Save dynamic ip address of local virtual machine

```
DOCKER_IP=$(docker-machine ip clicc)
```

4. Interact with the database (password: clicc)

```
psql -U clicc -W -h $DOCKER_IP
```
