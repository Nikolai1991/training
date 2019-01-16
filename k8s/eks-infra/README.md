###Create Namespaces
```
cd eks-infra/namespaces-and-secrets/namespaces/
kubectl apply -f namespaces.yaml
```
###Configure HPA
```
cd ../hpa/
kubectl create serviceaccount tiller --namespace kube-system
kubectl apply -f rbac-config.yaml
helm init --service-account tiller
kubectl get pods --namespace kube-system | grep tiller
```

###Configure metric-server
```
cd ../metrics-server/
kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default
helm install /home/ubuntu/trainning/eks-infra/metrics-server/ --name metrics-server --version 2.0.4 --namespace kube-system

# Check the health of Metrics server by using this command :
kubectl get apiservice v1beta1.metrics.k8s.io -o yaml

```

###Configure Cluster Autoscaler
```
cd ../cluster-autoscaler/
kubectl apply -f cluster_autoscaler.yml

```

###Deploy and Configure k8s nginx ingress controller
```
cd ../ingress-controller/
kubectl apply -f mandatory.yaml
kubectl apply -f patch-configmap-l7.yaml
kubectl apply -f service-l7.yaml

# Create external DNS and node-policy
chmod +x put-node-policy.sh        
./put-node-policy.sh               
kubectl apply -f external-dns.yaml 
```

###Ingress-Controller DNS
```
kubectl get svc -n ingress-nginx
```


