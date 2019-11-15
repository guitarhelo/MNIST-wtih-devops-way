
# Kubernetes & Image Registry

Objective :

* To use a image repository
* Deploy the image using Kubernetes

    Fun Fact : Why K8s?

    K u b e r n e t e s

    (K 1 2 3 4 5 6 7 8 s)    => K8s

## Prep - Installing Kubectl & PKS Commandlines

kubectl is just the command-line tool to send command to Kubernetes clusters.

This DOES NOT install the K8s server

Similar pks is the cli

Move the CLI for pks and kubectl to the right locations

    $ cd prerequisites
    $ cp pks /usr/local/bin
    $ cp kubectl /usr/local/bin

    $ cd /usr/local/bin

    $ sudo chmod +x kubectl
    $ sudo chmod +x pks

## Using the Registry

docker has capability to connect to a registry.  Push and Pull docker images from it.  Default is dockerhub.

Some sites has a private registry called *harbor*, deployed together with the PKS
Some sites would use the public dockerhub for this purpose

The registry each site would use is

| Location  | Container Registory   |   Username      |  Password
| --- | --- |  ---  |  --- |
| Beijing   | harbor.csc01.bjcsc.com | admin | P@ssw0rd |
| Shanghai  |                       |
| Singapore | harbor.csc-dell.com   | trainee01        | ********** |
|  Sydney   |                       |
| Tokyo     | Dockerhub             |                   |

### Trainees using Private registry (Harbor) - Sgp, Shg, Bj,Syd

#### Step 1

Because it is a private registry, and we didn't use a publicly signed key, we need this step to put the key in

    Copy the  ca.crt from your home directory to
    /etc/docker/certs.d/harbor.csc-dell.com/ca.crt

Login docker to registry (harbour)

    $ sudo docker login harbor.csc-dell.com

#### Step 2

We must name the local image properly, so that it can be pushed to the repository.

    $ sudo docker image ls

    $ sudo docker tag digitocr harbor.csc-dell.com/library/digitocr:<your name>1.0

    eg sudo docker tag digitocr harbor.csc-dell.com/library/digitocr:lmw1.0

    $ sudo docker image ls

Check that the repository is now "harbor.csc-dell.com/library/digitocr",  tag is "lmw1.0"

Now the image is still local.  To PUSH it to the remote repository, now

    $ sudo docker push harbor.csc-dell.com/library/digitocr:lmw1.0

### Trainees using public registry (Dockerhub) - Tokyo

#### Step 1

Docker by default assumes you uses dockerhub

Login docker to registry

    $ sudo docker login --username your-user-name

#### Step 2

Assuming you have already at dockerhub web UI, created a registry called 'trianing'

We must name the local image properly, so that it can be pushed to the repository.

    $ sudo docker image ls

    $ sudo docker tag digitocr username/training/digitocr:<your name>1.0

    eg sudo docker tag digitocr username/training/digitocr:lmw1.0

    $ sudo docker image ls

Now the image is still local.  To PUSH it to the remote repository, now

    $ sudo docker push username/training/digitocr:lmw1.0

## PKS/Kubernetes time

### Trainees using PKS (Sgp, Syd, Bj, Shg etc)

#### Creating the Kubernetes cluster

(this section should be skipped for trainee)

    pks login -a api.pks.csc-dell.com -u user2 -p P@ssw0rd -k

    pks plans

    pks clusters

    pks cluster training

To create a cluster

    (DO NOT DO IT)
    pks create-cluster training --external-hostname training.pks.csc-dell.com --plan small

Now access to the cluster

#### Working with the K8s cluster

Recap

* Where is your kubectl?

* Where is the K8s cluster?

* Think client-server.  How to connect to the right cluster?
  * <https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/>

    $ pks get-credentials training

    $ kubectl config use-context training

    $ kubectl cluster-info

### Trainees Using Micro Kubernetes (Tokyo)

(details information from your local person who set it up)

You need a config file to connect to the kubernetes

    Copy the file to .kube/config

    See the name of the cluster by doing <code> $ cat .kube/config</code>.  You would see the name uner <code>cluster: _____</code>

    $ kubectl config use-context name_of_cluster

Check that it works

    $ kubectl cluster-info

## Let's deploy

### Deploy using Deployment file

Creat a deployment.yaml file.  There is an example in the directory already.  

    Open it, edit the name of the container to what you need.

Deploy it

    $ kubectl apply -f deployment.yaml

Check that it is deployed

    $ kubectl get deployment

    $ kubectl get pods

Look into the details of the pod

    $ kubectl describe pod

### Now need to expose these outside the PODs

#### Method 1

    $  kubectl expose deployment name-of-deployment --name=loadbalancer --port=80 --target-port=80 --type=LoadBalancer

Note:

* --port =  the external port
* --target-port =  the internal port facing the containers

#### Method 2

    $ kubectl expose deployment/kubernetes-tutorial-deployment --type="NodePort" --port 80

Now ready to point to container to test.  But what is the IP address and Port?

What is the IP and PORT?

    $ kubectl describe nodes

You would see the IP of the cluster near the top

    $ kubectl get services

    See the line that says loadbalancer,  notice 80:xxxxx  .
    It exposed the port 80 to externally as port xxxx.  Need something else in front (reverse proxy etc)

So try connecting to the web page.

For reference

IP of the PKS cluster (nodes)

| Location  | IP
| --- | --- |
| Beijing   |                       |
| Shanghai  |                       |
| Singapore | 172.24.7.45  |
|  Sydney   |
| Tokyo     |

# Recap

* How many steps to do a deployment?
* would the deployment be repeatable?

------------------

Please ignore information below
Just some additional information

Connecting to Multiple Client

* use different contexts
* Basically, there is a .kube/config file which contains all the information
* Some commands to manage the context

    $ kubectl config current-context
    $ kubectl config get-contexts
    $ kubectl config use-context microk8s
    $ kubectl config use-context microk8s

This is installing the public version of kubectl

    sudo apt-get update && sudo apt-get install -y apt-transport-https
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
    sudo apt-get update
    sudo apt-get install -y kubectl

How to extract IP/Ports for exposing service. Scripting

    #get service website and ports for cscnginx
    export NODE_PORT=$(kubectl get svc -n default cscnginx -o jsonpath='{.spec.ports[0].nodePort}')
    export NODE_IP=$(kubectl get no -o jsonpath="{.items[0].status.addresses[0].address}")
    export APP_URL=http://$NODE_IP:$NODE_PORT/
    echo $APP_URL
