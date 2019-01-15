# Deploy and Configure k8s nginx ingress controller

Before you start please check this guide and use it as a reference so you will be updated.  

https://kubernetes.github.io/ingress-nginx/deploy/

###Step 1 - Usage instructions:

```
cd kops-k8s/ingress-controller/

# create nginx deployment + namespace for nginx-ingress + RBAC rules + any other mandatory resources the nginx ingress needs.

kubectl apply -f mandatory.yaml

# This setup requires to choose in which layer (L4 or L7) we want to configure the ELB:

1. Layer 4: use TCP as the listener protocol for ports 80 and 443.

2. Layer 7: use HTTP as the listener protocol for port 80 and terminate TLS in the ELB


For L7:
Change line of the file service-l7.yaml With your real certificate from AWS Certificate Manager "arn:aws:acm:us-west-2:XXXXXXXX:certificate/XXXXXX-XXXXXXX-XXXXXXX-XXXXXXXX"

Apply both of the yamls above.

kubectl apply -f service-l7.yaml
kubectl apply -f patch-configmap-l7.yaml
```

###Step 2 - Verify nginx installation:

```
kubectl get pods --all-namespaces -l app.kubernetes.io/name=ingress-nginx --watch

# Check nginx version:
chmod +x Check_nginx_version.sh
./Check_nginx_version.sh
```

###Step 2 - Working with Ingress controller:

```
To start using ingress controller you must edit your deployment manifest, change the service and add new kind called: ingress, this is example of how we using it : 
cat Dashboard_Service.yaml

# NOTE the ELB of nginx ingress controller doing the SSL termination in this case
```

# External DNS

Project page: https://github.com/kubernetes-incubator/external-dns

## Create IAM Policy
```
./put-node-policy.sh
```

## Create external DNS and ingress rules
```
kubectl apply -f external-dns.yaml
kubectl apply -f <SOME_APP>
```

