#
# Outputs
#

locals {
  config_map_aws_auth = <<CONFIGMAPAWSAUTH


apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles: |
    - rolearn: ${aws_iam_role.eks-cluster-node.arn}
      username: system:node:{{EC2PrivateDNSName}}
      groups:
        - system:bootstrappers
        - system:nodes
CONFIGMAPAWSAUTH

  kubeconfig = <<KUBECONFIG


apiVersion: v1
clusters:
- cluster:
    server: ${aws_eks_cluster.eks-cluster.endpoint}
    certificate-authority-data: ${aws_eks_cluster.eks-cluster.certificate_authority.0.data}
  name: "${aws_eks_cluster.eks-cluster.arn}"
contexts:
- context:
    cluster: "${aws_eks_cluster.eks-cluster.arn}"
    user: "${aws_eks_cluster.eks-cluster.arn}"
  name: ${var.customer}-${var.cluster-name}
current-context: ${var.customer}-${var.cluster-name}
kind: Config
preferences: {}
users:
- name: "${aws_eks_cluster.eks-cluster.arn}"
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1alpha1
      command: aws-iam-authenticator
      args:
        - "token"
        - "-i"
        - "${var.cluster-name}"
KUBECONFIG
}

output "config_map_aws_auth" {
  value = "${local.config_map_aws_auth}"
}

output "kubeconfig" {
  value = "${local.kubeconfig}"
}

output "cluster_arn" {
  value = "${aws_eks_cluster.eks-cluster.arn}"
}
