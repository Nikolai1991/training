###Create Namespaces
```
cd kops-infra/namespaces-and-secrets/namespaces/
kubectl apply -f namespaces.yaml
```

###Configure metric-server
```
cd ../../metrics-server/
kubectl apply -f auth-delegator.yaml
kubectl apply -f auth-reader.yaml
kubectl apply -f metrics-apiservice.yaml
kubectl apply -f metrics-server-deployment.yaml
kubectl apply -f metrics-server-service.yaml
kubectl apply -f resource-reader.yaml
```

###Configure HPA
```
cd ../hpa/
kubectl create serviceaccount tiller --namespace kube-system
kubectl apply -f rbac-config.yaml
helm init --service-account tiller
kubectl get pods --namespace kube-system | grep tiller
```

###Configure Cluster Autoscaler
```
cd ../cluster-autoscaler/
chmod +x cluster-autoscaler.sh
./cluster-autoscaler.sh
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

