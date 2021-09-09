terraform {
  backend "s3" {
    bucket = "jfreeman-todo-backend"
    key    = "todo-backend-${var.branch_name}"
    region = "ap-southeast-2"
  }
}

/* Static Website */


/* RDS Instance */


/* AWS Secrets for RDS Instance */


/* Helm Release */

