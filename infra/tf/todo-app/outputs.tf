output "db_root_user_secretsmanager_name" {
  value       = aws_secretsmanager_secret.db_credentials_secret[0].name
  description = "Name of secretsmanager secret containing master / root user password for rds instance"
}

output "db_todo_user_secretsmanager_name" {
  value       = aws_secretsmanager_secret.db_credentials_secret[1].name
  description = "Name of secretsmanager secret containing todo user password for rds instance"
}

output "rds_endpoint" {
  value       = module.db.db_instance_endpoint
  description = "description"
}

output "rds_root_user" {
  value       = module.db.db_instance_username
  description = "Master username for RDS instance"
}

output "s3_bucket_name" { value = module.website.s3_bucket_name }

output "cloudfront_dist_id" { value = module.website.cloudfront_dist_id }