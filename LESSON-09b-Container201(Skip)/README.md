# Building a container with Apache server

## Step 1

In a new directory.

Creat a file named <code>Dockerfile</code> with the follow content

    FROM ubuntu:18.04
    MAINTAINER lmw <lmw@lmw>

    RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*
    ENV APACHE_RUN_USER  www-data
    ENV APACHE_RUN_GROUP www-data
    ENV APACHE_LOG_DIR   /var/log/apache2
    ENV APACHE_PID_FILE  /var/run/apache2/apache2.pid
    ENV APACHE_RUN_DIR   /var/run/apache2
    ENV APACHE_LOCK_DIR  /var/lock/apache2
    ENV APACHE_LOG_DIR   /var/log/apache2
    RUN mkdir -p $APACHE_RUN_DIR
    RUN mkdir -p $APACHE_LOCK_DIR
    RUN mkdir -p $APACHE_LOG_DIR

    COPY index.html /var/www/html

    EXPOSE 80

    CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]

Create a file named 'index.html', with following contents

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>First APP</title>
    </head>
    <body>

        <h1>My first attempt to create a docker container</h1>

    </body>
    </html>

Check that you have the 2 files in the directory
* Dockerfile
* index.html

Let's pause to understand what we are doing.

## Step 2

    $ docker build --tag=secondcontainer .

See the response, comparing with your Dockerfile

    $ docker image ls

Notice the new images there.  Also the Ubuntu 18.04 image.

## Step 3 Now run the container

    $ docker run -p 4000:80 -d fsecondcontainer

Check it out at the browser


