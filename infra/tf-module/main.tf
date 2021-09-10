/*
terraform {
  backend "s3" {
    bucket = "jfreeman-todo-backend"
    key    = "todo-backend-${var.branch_name}"
    region = "ap-southeast-2"
  }
}
^ Will need to be templated.. :(

*/

/* Static Website */

module "website" {
  source  = "git@github.com:jxeldotdev/tf-s3-static-website.git"
  domains = ["${var.frontend_domain}.jxel.dev", "www.${var.frontend_domain}.jxel.dev"]
}


/* RDS Instance */


/* AWS Secrets for RDS Instance */


/* Helm Release */

