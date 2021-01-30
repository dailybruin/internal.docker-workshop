# Docker/docker-compose.yml workshop

Things we will cover:
1. What is docker? Why is it useful?
2. Images, Containers
3. Image construction
4. Container life cycle
5. File systems of containers
6. Volumes
7. docker-compose.yml

## Useful commands

Starts a container from image `IMAGE_ID` and runs `<command>` in it

```
docker run -it IMAGE_ID <command>
```

Builds a docker image with context = current directory

```
docker build .

```

