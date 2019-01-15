provider "aws" {
  region  = "eu-west-1"
  profile = "default"
}

terraform {
  backend "s3" {
    bucket  = "__BUCKET_NAME__"
    key     = "__CLUSTER_NAME__-build-__BUILD_NUMBER__/tfstate/terraform.tfstate"
    region  = "eu-west-1"
    profile = "default"
  }
}
