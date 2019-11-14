# Some common commands for docker

## List Docker CLI commands

* docker
* docker container --help

## Display Docker version and info

* docker --version
* docker version
* docker info

## Execute Docker image

* docker run hello-world

* docker stop
* docker kill
* docker container rm

* sudo docker rm $(sudo docker ps -a -f status=exited -q)

## List Docker images

* docker image ls

## List Docker containers (running, all, all in quiet mode)

* docker container ls
* docker container ls --all
* docker container ls -aq
* docker ps -a

## Debugging - To get a shell

* docker exec -it "container name" /bin/bash

## To copy a docker image to another machine without using repository

* Step 1.  To save the image
  
    docker image save NAME > filename.tar

* Step 2.  In the new machine

    docker image load --input filename.tar

## To use a repository

* docker push  repository:tag

## To Save a CONTAINER

* sudo docker save -o ./cleverexport  clever
