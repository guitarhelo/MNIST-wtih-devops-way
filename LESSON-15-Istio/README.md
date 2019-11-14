# Service Mesh (with Istio)

## Enabling Istio on PKS

### Step 1 - Create New cluster

<https://blogs.vmware.com/cloudnative/2019/03/12/integrating-istio-vmware-enterprise-pks/>

Here is summary of the steps
Creat Netowrk Profile file, call it "network-profile-medium.json"

    {"description": "network profile with medium size LB",
        "name": "network-profile-medium",
        "parameters": {
        "lb_size": "medium"
        }
        }

    $ pks create-network-profile network-profile-medium.json

Create new cluster using the network profile

    $   pks create-cluster training --external-hostname training.pks.csc-dell.com --plan medium --num-nodes 4 --network-profile network-profile-medium

Get credentials and try connecting to it

    $ pks get-credentials training

    $ kubectl use-context training

Check the cluster is working

    $ kubectl get nodes -o wide

### Step 2- Now download and install Istio

Download the Istio bits and add its binary location to the PATH variable. Execute the following command to download Istio:

    $ sudo curl -L https://git.io/getLatestIstio | sh -

See <https://istio.io/docs/setup/kubernetes/install/> to add Istio to your Kubernetes cluster.

To configure the istioctl client tool for your workstation,
add the /home/trainee/istio-1.3.2/bin directory to your environment path variable with:

    $ export PATH="$PATH:/home/trainee/istio-1.3.2/bin"

Begin the Istio pre-installation verification check by running:

    $ istioctl verify-install

Start to install Istio CRD (Custom Resource Definitions)

    $ cd istio-1.3.2

    $ for i in install/kubernetes/helm/istio-init/files/crd*yaml; do kubectl apply -f $i; done

    $ kubectl apply -f install/kubernetes/istio-demo.yaml

Checking

    $ kubectl get svc -n istio-system

    $ kubectl get pods -n istio-system

### Step 3 - Market the cluster for istio enabled

Must use the namespace that has istio-injection=enabled

Option 1)  Change existing default

    $ kubectl label namespace default istio-injection=enabled

Option 2) Create new namespace

    $ kubectl create namespace training-withistio

    $ kubectl label namespace <namespace> istio-injection=enabled

    $ kubectl apply yourdeployment.yaml -n training-withistio

    $ kubectl get pods -n training-withistio

------
    (this instruction below didn't work for me.  Need to debug)
    To create a enw context that would point to that namespace

    Must now associate the namespace with a specific context
    $ kubectl config current-context
    $ kubectl config set-context trainingistio --namespace=training-withistio \
        --cluster=microk8s \
        --user=microk8s

    $ kubectl config use-context trainingistio

    $ kubectl create -n <namespace> -f <your-app-spec>.yaml
