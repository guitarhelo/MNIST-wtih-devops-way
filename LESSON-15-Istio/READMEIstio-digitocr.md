# Deploy Containers with Istio

The genreal steps to change a normal kubernetes .yaml file to work for istio
1.  Modify the YAMAL files to tag version to each application
2.  Create a destination rule yaml
3.  Create virtual service that routes selectively

## Step 1

Have made modification to the YAML files from normal kubernetes deployment. Using the provided YAML files

Let's deploy all the containers, services just like Kubernetes case

    $ kubectl apply -f deploymentDockerHub.yaml

    $ kubectl apply -f deploymentdockerhub-services-2version.yaml

Check to see what is happening

    $ kubectl get pods

Notice how many containers inside each POD?  2/2?
If you get into the details using 'kubectl describe pods digitocr-...', you would see

    istio-proxy:
        Container ID:  containerd://f46d5fba02a7b76543c7f2f4d01b928ede0cac241ae2811c277fca39d01b80dc
        Image:         docker.io/istio/proxyv2:1.3.2
        Image ID:      docker.io/istio/proxyv2@sha256:6a7d338b8da5a99574f0a78195da974d895ad6b65682660b1717c43e6b7559e6
        Port:          15090/TCP
        Host Port:     0/TCP


At this stage, the deployment should be working as before.  The Istio sidecars are deployed automatically, but it doesn't affect the routing

## Step 2

Now, apply destination rules

    kubectl apply -f destination-rule-all.yaml

Can now change the weightage to each route by by Virtual Service

    kubectl apply -f route-rules.yaml

Go into the file to adjust the weight. And refresh the web page to see how many times it hit v1 versus v2.