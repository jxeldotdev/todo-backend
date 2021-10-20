locals {
  tags = {
    branch      = var.branch_name
    environment = var.environment
    app         = "todo"
    managed-by  = "Terraform"
  }
}


/* Static Website / Frontend */

module "website" {
  source            = "git@github.com:jxeldotdev/tf-s3-static-website.git"
  domains           = [var.frontend_url, "www.${var.frontend_url}"]
  zone_id           = var.cf_zone_id
  bucket_name       = "frontend-${var.branch_name}-${var.environment}"
  service_role_name = "frontend-${var.branch_name}-${var.environment}"
}

/* AWS Secrets for RDS Instance */

resource "random_password" "db_master_password" {
  length           = 32
  special          = true
  override_special = "_%@"
}


resource "random_password" "db_todo_password" {
  length           = 32
  special          = true
  override_special = "_%@"
}


resource "aws_secretsmanager_secret" "db_credentials_secret" {
  for_each = ["root-user", "todo-user"]
  name     = "todo-backend-${each.key}-db-credentials-${var.branch_name}"
}

resource "aws_secretsmanager_secret_version" "db_credentials_secret" {
  for_each  = ["root-user", "todo-user"]
  secret_id = aws_secretsmanager_secret.db_credentials_secret[each.key].id
  secret_string = jsonencode({
    username = each.value
    password = random_password.db_master_password.result
  })
}

data "aws_secretsmanager_secret_version" "db_secret" {
  secret_id = aws_secretsmanager_secret.db_credentials_secret.id
}


data "aws_subnet_ids" "db" {
  vpc_id = var.vpc_id
  tags = {
    app          = "todo"
    managed-by   = "Terraform"
    environement = var.environment
    tier         = "database"
  }
}

data "aws_security_groups" "database" {
  tags = {
    app        = "todo"
    managed-by = "Terraform"
    tier       = "database"
  }

  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }
}

/* RDS Instance */
module "db" {
  source = "terraform-aws-modules/rds/aws"

  identifier = "todo-${var.branch_name}-${var.environment}-db"

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

  multi_az               = var.is_multi_az
  subnet_ids             = data.aws_subnet_ids.db.ids
  vpc_security_group_ids = data.aws_security_groups.database.ids
  db_subnet_group_name   = var.db_subnet_group_name

  maintenance_window              = "Mon:00:00-Mon:03:00"
  backup_window                   = "03:00-06:00"
  enabled_cloudwatch_logs_exports = ["postgresql", "upgrade"]

  backup_retention_period               = var.backup_retention_period
  skip_final_snapshot                   = true
  deletion_protection                   = var.deletion_protection
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