# Using Kubernetics for deployment

**This is NOT used in the training.  This is for using with a local kunernetes installation, docker hub**

** This file is here for for my info **


    Creat a deployment.yaml file

    $ kubectl apply -f deployment.yaml

Check that it works  

    $ kubectl get pods

Need to expose the container to external

example command 1

    $ kubectl expose deployment kubernetes-tutorial-deployment --name=loadbalancer --port=80 --target-port=8080 --type=LoadBalancer

> --port =  the external port

> --target-port =  the internal port facing the containers

example command 2

    $ kubectl expose deployment/kubernetes-tutorial-deployment --type="NodePort" --port 80

To check the details

    $ kubectl describe services/kubernetes-tutorial-deployment

    $ kubectl get services


** NOTE - If using private registry.  Must use kubenetes specific method to access the docker hub.  For example **imagePullSecrets**  (https://kubernetes.io/docs/concepts/containers/images/#referring-to-an-imagepullsecrets-on-a-pod)

Steps 1  - run the following command, replace UPPER CASE with suitable values

kubectl create secret docker-registry <name> --docker-server=DOCKER_REGISTRY_SERVER --docker-username=DOCKER_USER --docker-password=DOCKER_PASSWORD --docker-email=DOCKER_EMAIL

Step 2 - In the POD yaml file, add in section with container definition

  imagePullSecrets:
    - name: myregistrykey

