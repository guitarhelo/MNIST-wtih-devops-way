# Build your project in Docker

## Step 1

Create on Ubuntu directory 'les##'

Copy all the files in 'LESSON-xx-....' from windows over to the new directory

app.py is the main app
     It uses the flask framwork for a web interface
     If you just run app.py, the port is 4555

     In this case, we are going to deploy using a Apache web server


## Step 2.  Go through the Dockerfile

* Uses a Apache server (to replace the development server in Flask)

* Build all the dependencies

* Copy all the files over

## Step 3

You should know how to do it

    build the container

    run the container

Check that the web page works

Hint :
What is the port that the container would try to connect to? 4555 as stated in the app?
Try to deploy the container to access from port 5001

How Webserver interface with the Python code
WSGI

# Recap

