# Deploy Metrics-Server


###Step 1 - Usage instructions:
```
cd niko-k8s/kops-infra/metrics-server/

kubectl apply -f auth-delegator.yaml

kubectl apply -f auth-reader.yaml

kubectl apply -f metrics-apiservice.yaml

kubectl apply -f metrics-server-deployment.yaml

kubectl apply -f metrics-server-service.yaml

kubectl apply -f resource-reader.yaml

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
