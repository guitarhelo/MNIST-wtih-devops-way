
# Build your own container

Since we have been doing Python programming, let's build a container to run the python codes

On the ubuntu

    create a new directory called 'les##'  (replace ## with lesson number)

    cd to the directory


## Step 1  Write some Python codes that you want to deploy

Create a file named 'app.py', with following contents

    from flask import Flask, request
    from datetime import datetime
    import os
    import socket

    app = Flask(__name__)

    @app.route("/")
    def hello():

        html = "<h3>Hello My {name}!</h3>" \
            "<b>Hostname:</b> {hostname}<br/>" \
            "<b>IP:</b> {hostip}<br/>" \
            "<b>DateTime:</b> {datetimenow}<br/>"

        return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), hostip=request.host, datetimenow=datetime.now())

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)

You can try to run the code.  Error?  Hint
* because of venv, 
* maybe need to sudo (due to port 80)

Use a chrome to point to check that it works

## Step 2  Create *dockerfile*

Creat a file named <code>Dockerfile</code> with the follow content

    # Use an official Python runtime as a parent image
    FROM python:3.7-slim

    # Set the working directory to /app
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    #RUN pip install --trusted-host pypi.python.org -r requirements.txt
    RUN pip3 install -r requirements.txt

    # Make port 80 available to the world outside this container
    EXPOSE 80

    # Define environment variable
    ENV NAME World

    # Run app.py when the container launches
    CMD ["python", "app.py"]


Create a file named <code>requirements.txt</code>, with the following content

    Flask

Check that you have the  files in the directory
* Dockerfile
* app.py
* flask

Let's pause to understand what we are doing.

## Step 3 Build container image

    $ docker build --tag=firstimage .

See the response, does it match your Dockerfile?

    $ docker image ls


## Step 4 Now run the container

    $ docker run -p 4000:80 -d firstimage

Notice this time we use -p, not -P.  You can guess what that option means.

Check it out at the browser

# Recap

Easy?

How to make sure consistency in deployment?  (DevOps)