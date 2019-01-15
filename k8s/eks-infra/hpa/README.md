# Configure HPA

Before you can start you need to deploy tiller (Service account for Helm) by using this guide: https://medium.com/@zhaimo/using-helm-to-install-application-onto-aws-eks-36840ff84555

###Step 1 - Usage instructions:
```

cd training/eks-infra/hpa/

wget https://storage.googleapis.com/kubernetes-helm/helm-v2.12.1-linux-amd64.tar.gz

tar xvf helm-v2.12.1-linux-amd64.tar.gz 

cd linux-amd64/

sudo cp helm /usr/local/bin/

helm init --upgrade

# check helm version // wait until it will work
# Now let’s create a tiller service account (Tiller is the Helm server-side component)


kubectl create serviceaccount tiller --namespace kube-system

kubectl apply -f rbac-config.yaml

helm init --service-account tiller

kubectl get pods --namespace kube-system | grep tiller
```

###Step 2 - HPA-TEST:
```
# Deploy a Sample App
kubectl run php-apache --image=k8s.gcr.io/hpa-example --requests=cpu=200m --expose --port=80

# Create an HPA resource
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10

kubectl get hpa

# Generate load to trigger scaling
kubectl run -i --tty load-generator --image=busybox /bin/sh

while true; do wget -q -O - http://php-apache; done

kubectl get hpa -w

https://eksworkshop.com/images/scaling-hpa-results.png
```
