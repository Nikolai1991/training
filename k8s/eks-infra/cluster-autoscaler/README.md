# Configure HPA

###Step 1 - Usage instructions:

```
git clone https://nikolai1991@bitbucket.org/nikolai1991/niko-k8s.git

cd niko-k8s.git/eks-infra/cluster-autoscaler/

kubectl apply -f cluster-autoscaler.yml

# please change the --node command at cluster-autoscaler.yml file
# --nodes=2:6:nodes.kubernetes.nikolaidavidov.com
# --nodes={{MIN_NODES}}:{{MAX_NODES}}:{{ASG_NAME}}
```

###Step 2 - Cluster-Autoscaler-TEST:

```
# Test Cluster auto scaler operation: Deploy php-apache container with 50 Replicas to check the auto scaler. 
kubectl run php-apache --image=k8s.gcr.io/hpa-example --requests=cpu=200m --expose --port=80 --replicas=50

# Check logs and kubectl get nodes and look for Auto scaler desired instances number it should be changed according to auto scaler definition
```

