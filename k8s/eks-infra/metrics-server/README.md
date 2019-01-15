# Deploy Metrics-Server Helm Chart 


###Step 1 - Usage instructions:
```
git clone https://nikolai1991@bitbucket.org/nikolai1991/niko-k8s.git

cd niko-k8s/eks-infra/metrics-server/

kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default

helm install /home/ubuntu/k8s/server-metrics-helm-chart-eks/metrics-server/ --name metrics-server --version 2.0.4 --namespace kube-system

# Check the health of Metrics server by using this command :

kubectl get apiservice v1beta1.metrics.k8s.io -o yaml
```
###Step 2 - Metrics-server test:
```
# create some app and run the command "kubectl top pod/node"

Display Resource (CPU/Memory/Storage) usage.

The top command allows you to see the resource consumption for nodes or pods.

This command requires Heapster to be correctly configured and working on the server.

Available Commands:
  node        Display Resource (CPU/Memory/Storage) usage of nodes
  pod         Display Resource (CPU/Memory/Storage) usage of pods

Usage:
  kubectl top [flags] [options] 
```


