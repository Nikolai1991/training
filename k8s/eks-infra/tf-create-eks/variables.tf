#
# Variables Configuration
#

#var.environment
variable "environment" {
  type    = "string"
}

#var.customer
variable "customer" {
  type    = "string"
}

#var.cluster-name
variable "cluster-name" {
  type    = "string"
}

#var.vpc_id
variable "vpc_id" {
  default = ""
  type    = "string"
}

#var.master_subnet_ids
variable "master_subnet_ids" {
  type    = "list"
}

#var.node_subnet_ids
variable "node_subnet_ids" {
  type    = "list"
}

#var.instance_type
variable "instance_type" {
  default = "m4.large"
  type    = "string"
}

#var.ssh_key_name
variable "ssh_key_name" {
  default = ""
}

#var.root_volume_size
variable "root_volume_size" {
  default = "50"
}

#var.min_nodes
variable "min_nodes" {
  default = "2"
  type    = "string"
}

#var.max_nodes
variable "max_nodes" {
  default = "10"
  type    = "string"
}

#var.vpn_ssl_pool
variable "vpn_ssl_pool" {
  description = "The VPN SSL pool, to allow SSH from"
  default     = ""
}
