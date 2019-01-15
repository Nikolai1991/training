# EKS Getting Started Guide Configuration

This is the full configuration from https://www.terraform.io/docs/providers/aws/guides/eks-getting-started.html

See that guide for additional information.

NOTE: This full configuration utilizes the [Terraform http provider](https://www.terraform.io/docs/providers/http/index.html) to call out to icanhazip.com to determine your local workstation external IP for easily configuring EC2 Security Group access to the Kubernetes master servers. Feel free to replace this as necessary.

# terraform-aws-eks

A terraform module to create a managed Kubernetes cluster on AWS EKS. Available
through the [Terraform registry](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws).
Inspired by and adapted from [this doc](https://www.terraform.io/docs/providers/aws/guides/eks-getting-started.html)
and its [source code](https://github.com/terraform-providers/terraform-provider-aws/tree/master/examples/eks-getting-started).
Read the [AWS docs on EKS to get connected to the k8s dashboard](https://docs.aws.amazon.com/eks/latest/userguide/dashboard-tutorial.html).

## Prerequesits
* Install kubectl
https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
* Install aws-iam-authenticator
https://docs.aws.amazon.com/eks/latest/userguide/configure-kubectl.html
* Install terraform
https://www.terraform.io/intro/getting-started/install.html

## Assumptions
* You have a bitbucket ssh key configured in order to get the module
* You want to create an EKS cluster and an autoscaling group of workers for the cluster.
* You want these resources to exist within security groups that allow communication and coordination.
* You've created a Virtual Private Cloud (VPC) and subnets where you intend to put the EKS resources.
* You've completed the Prerequesits.

## Usage example

```hcl
module "eks" {
  source                = "git@bitbucket.org:emindsys/tf-eks-module.git" //Source of module
  cluster_name          = "test-eks-cluster" //eks cluster name
  environment           = "production" //environment of cluster
  vpc_id                = "vpc-abcde012" //vpc id of where cluster should be launched
  master_subnet_ids     = ["subnet-abcde012", "subnet-bcde012a"] //subnet ids for the master nodes
  node_subnet_ids       = ["subnet-abcde012", "subnet-bcde012a"] //subnet ids for the worker nodes
  instance_type         = "m5.large" //instance type of the worker nodes
  ssh_key_name          = "prod-eks" //ssh key pair to be used with the worker nodes
  root_volume_size      = "50" //volume size of the root volume on the worker nodes
  min_nodes             = "3" //minimum nodes in the cluster
  max_nodes             = "10" //maximum nodes in the cluster for autoscaling
  vpn_ssl_pool          = "192.168.255.0/24" //the vpn CIDR to allow ssh to the worker nodes
}
```

## Usage instructions
###Step 1:
 Install aws-iam-authenticator for Amazon EKS
```
curl -o aws-iam-authenticator  https://amazon-eks.s3-us-west-2.amazonaws.com/1.11.5/2018-12-06/bin/linux/amd64/aws-iam-authenticator

chmod +x ./aws-iam-authenticator

export KUBECONFIG=~/.kube/config 

cp ./aws-iam-authenticator /bin/aws-iam-authenticator && export PATH=/bin:$PATH

aws-iam-authenticator // test

```
###Step 2:
 Copy the above example to your terraform code and replace the variables as you wish and run terraform.
###Step 3:
 Once done, configure kubectl config from the terraform output starting from:
"kubeconfig =...."
###Step 4:
 Validate EKS Clster.
```
vim ~/.kube/config // copy from the output

export AWS_PROFILE=default // if needed

export KUBECONFIG=~/.kube/config 

vim config_map_aws_auth.yaml // copy from the output

kubectl create -f config_map_aws_auth.yaml

```
###Step 5:
 make sure kubectl is working:
```
kubectl get pods --all-namespaces

kubectl get nodes -o yaml

```
You should get at least 1 namespace.
###Step 6:
 Once kubectl is configured and working, create the configmap from the terraform output so nodes will be discovered by the masters. 
Starting from: config_map_aws_auth = ......
make sure nodes are added by running the following command:
```
kubectl get nodes --output=wide

```
You should get the list of the nodes that you've created.
###Step 7:
 That's it! If you've reached this point then your cluster is ready. Now you can do as you wish, for example: create an ingress controller, enable dashboard, etc...


## Helpful Links Attached:
* Deploy the Kubernetes Web UI (Dashboard) - https://docs.aws.amazon.com/eks/latest/userguide/dashboard-tutorial.html
* Deploy the nginx-ingress controller - https://github.com/kubernetes/ingress-nginx/tree/master/deploy

