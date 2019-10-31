# Containers

We would be using Docker containers  (that is like the defacto standard.  Not the only one)

*  Eg, PAS actually uses Garden container services.  Not Docker

## Install Docker

Using the Ubuntu for this exercise

To Install Docker on Ubuntu
See instructions at
https://docs.docker.com/install/linux/docker-ce/ubuntu/


### Step 1 - add the repository

    $ sudo apt-get remove docker docker-engine docker.io containerd runc

    $ sudo apt-get update

    $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common

    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    $ sudo apt-key fingerprint 0EBFCD88

    $ sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

### Step 2 - install Docker from the repository

    $ sudo apt-get update

    $ sudo apt-get install docker-ce docker-ce-cli containerd.io


### Step 3 - Verify installation


    $ docker --version

See version 19.03.2?

    $ docker run hello-world


*NOTE: *

*PROXY SERVER*  If you need proxy server, please see READMEproxy.md

See the response.  Let's understand what happened at the back.  Cool right?  So much things done automatically

Where was the container stored?  How did it magically appeared?

    $ docker image ls

    $ docker images hello-world

    $ docker container ls --all

Note : What's an *image*, what's a *container*

You have just deployed a Hello-world container

## Hands-on with Docker

### Step 1 Let's run a demo nginx web server

    $ docker run -P -d nginxdemos/hello

What are those -P -d options?
How to see the *help*?

    $ docker run --help | more


[ACTION]
    Find the container running

    Can you figure out how to access the web page that it serves?


    $ docker container list


Try to deploy more of the same container
Do the same common again to deploy a second copy of the image

    $ docker run -P -d nginxdemos/hello

Go access it.  And see that both web pages are alive
* Notice the internal IP address
* Notice the port number

### Step 2 Stopping the container

What command do you think you can use to do that?
    * are you working with image or container?
    * so..... sudo docker container.......
    * how to get the help?


    $ sudo docker container list
    $ sudo docker container stop xxxxxxxx

Is the container gone?

    $ sudo docker ps

(this is equipvilent to *docker container lsit* )

    $ sudo docker ps -la

    $ sudo docker rm xxxxxxx

Now, confirm it is gone :)

# Recap

Simple to install?

Simple to deploy container?
