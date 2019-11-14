
# Kubernetes - Microservice

The DigitOCR was was seperated two 2 parts, 1 frontend, 1 backend with RESTAPI

Objective

* Containerise the 2 apps
* Deploy using kubernetes

## Steps 1 - Build the containers

There are two directories one for the front-end, on the api microservice

### API Microservice

Let's build based on Python container.  We will use the built-in flask server.

     Check which port the app is listening for.  
     Make it 80.  Since it is afterall, an http service.

     Help from :   https://hub.docker.com/_/python

     use the image python for 3.6-slim-buster

     please name the container : harbor.csc-dell.com/library/digitocr-api-service:1.0

Run the container, and use a web server/Insomnia to check it is working

### The frontend APP

Some minor change to the code

     It should serve port 80.

What address to use to access the web service?  Our earlier code points to fixed IP.

     Tag the container as  harbor.csc-dell.com/library/digitocr-frontend:1.0 

     sudo docker build -t harbor.csc-dell.com/library/digitocr-frontend:1.0 .

## Step 2 - Prepare Kubernetes deployment

### Push the image to harbor registry

     $ sudo docker push harbor.csc-dell.com/library/digitocr-frontend:1.0

     $ 

### the YAML files

## Step 3 - Deploy

    kubectl apply -f deployment.yaml

## Step 4 - Canary Deployment (using native Kubernetes)

DevOps - How to quickly test apps while managing risk.  

If you want to learn the example by yourself  
     <https://github.com/ContainerSolutions/k8s-deployment-strategies/tree/master/canary/native>

Else, here is the instruction

Your should show still have the digitocr-service-v1 deployed, 2 replicas.  Confirm that by
     $ kubectl get deployment

     else 

     $ kubectl apply -f deploymentDockerhub.yaml

Please access the app, and see the response from the restapi says *ver 1*

Let's build and deploy another version of the app

     You need to edit the appapi-file.py file to change the line 

          APP_VER = 1.0

          change to 

          APP_VER = 2.0
          
     Build the container

     $    sudo docker build -t harbor.csc-dell.com/library/digitocr-frontend:2.0 .

Let's deploy another version of the app

     Creat another copy of the deployment file.

     Edit the yaml file to point to the version 2 container, and also the deployment name to -v2 instead of -v1. (there should be 2 changes).  
     Warning.  Not change the API version value

Now access the webpage, repeat a few times and see how often you get Ver1, how often ver 2.

     Scale up the version 2

          $ kubectl scale --replicas=10 deploy digitocr-service-v2

     Scale down the version 1 to 1 replica

          $ kubectl scale --replicas=1 deploy digitocr-service-v1

     Delete v1 deployment

          $ kubectl delete deployment digitocr-service-v1

# Recap
