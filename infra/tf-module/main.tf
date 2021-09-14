
# ENVIRONMENT and BRANCH_NAME are substituted with environment variables :)
terraform {
  backend "s3" {
    bucket = "jfreeman-todo-backend-${ENVIRONMENT}"
    key    = "todo-backend-${BRANCH_NAME}"
    region = "ap-southeast-2"
  }
}

locals {
  tags = {
    branch = var.branch_name
    environment = var.environment
    app = "todo"
    managed-by = "Terraform"
  }
}


/* Static Website / Frontend */

module "website" {
  source      = "git@github.com:jxeldotdev/tf-s3-static-website.git"
  domains     = ["${var.frontend_domain_prefix}.jxel.dev", "www.${var.frontend_domain_prefix}.jxel.dev"]
  zone_id     = var.cf_zone_id
  bucket_name = "frontend-${var.branch_name}-${var.environment}"
  service_role_name = "frontend-${var.branch_name}-${var.environment}"
}

/* Helm Release - Deploys the API */


resource "helm_release" "backend" {
  name       = "todo-backend-${var.branch_name}-${var.environment}"
  chart      = "../todo-backend/"
  
  set {
    name  = "image.tag"
    value = var.docker_image_tag
  }

  set {
    name  = "config.PostgresDB"
    value = var.db_name
  }

  set {
    name  = "config.postgresHost"
    value = module.db.db_instance_endpoint
  }

  set {
    name = "config.corsAllowedOrigins"
    value = "${var.frontend_domain_prefix}.jxel.dev,www.${var.frontend_domain_prefix}.jxel.dev"
  }

  set {
    name = "db.password"
    value = data.aws_secretsmanager_secret_version.db_secret.secret_string
  }

  depends_on = [module.db]
}

/* AWS Secrets for RDS Instance */

resource "random_password" "db_master_password" {
  length           = 32
  special          = true
  override_special = "_%@"
}


resource "aws_secretsmanager_secret" "db_credentials_secret" {
  name = "todo-backend-db-credentials-${var.branch_name}"
}

resource "aws_secretsmanager_secret_version" "db_credentials_secret" {
  secret_id     = aws_secretsmanager_secret.db_credentials_secret.id
  secret_string = random_password.db_master_password.result
}

data "aws_secretsmanager_secret_version" "db_secret" {
  secret_id     = aws_secretsmanager_secret.db_credentials_secret.id
}


data "aws_subnet_ids" "db" {
  vpc_id = var.vpc_id
  tags = {
    app = "todo"
    managed-by = "Terraform"
    environement = var.environment
    tier = "database"
  }
}

data "aws_security_group" "selected" {
  id = var.security_group_id
}

/* RDS Instance */
module "db" {
  source = "terraform-aws-modules/rds/aws"

  identifier = "todo-${var.environment}-${var.branch_name}-db"

  engine               = "postgres"
  engine_version       = "13.3"
  family               = "postgres13" # DB parameter group
  major_engine_version = "13"         # DB option group
  instance_class       = var.db_instance_class

  allocated_storage     = 10
  max_allocated_storage = 50
  storage_encrypted     = true

  name     = var.db_name
  username = var.master_db_user
  password = data.aws_secretsmanager_secret_version.db_credentials_secret.secret_string
  port     = 5432

  multi_az               = (var.environment = "production" ? true : false)
  subnet_ids             = data.aws_subnet_ids.db.ids
  vpc_security_group_ids = [var.db_sg_ids]
  db_subnet_group_name   = 

  maintenance_window              = "Mon:00:00-Mon:03:00"
  backup_window                   = "03:00-06:00"
  enabled_cloudwatch_logs_exports = ["postgresql", "upgrade"]

  backup_retention_period = var.backup_retention_period
  skip_final_snapshot     = true
  deletion_protection     = (var.environment = "production" ? true : false)

  performance_insights_enabled          = true
  performance_insights_retention_period = 7
  create_monitoring_role                = true
  monitoring_interval                   = 60
  monitoring_role_name                  = var.db_monitoring_role_name
  monitoring_role_description           = "Description for monitoring role"

  parameters = [
    {
      name  = "autovacuum"
      value = 1
    },
    {
      name  = "client_encoding"
      value = "utf8"
    }
  ]
} 
