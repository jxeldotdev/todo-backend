provider "aws" {
  region = "ap-southeast-2"
  default_tags {
    tags = {
      Environment = "${ENVIRONMENT}"
      Account     = "${ENVIRONMENT}"
      Application = "Todo-App"
      Managed-By  = "Terraform"
      Owner       = "Ops"
    }
  }
  assume_role {
    role_arn = var.iam_role_arn
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">=3.40"
    }
  }
  backend "s3" {
    bucket         = "${TFSTATE_BUCKET}"
    key            = "terraform.tfstate"
    region         = "ap-southeast-2"
    dynamodb_table = "${TFSTATE_TABLE}"
  }
}
