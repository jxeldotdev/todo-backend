/* Create RDS instance, Frontend deployment and AWS Secrets.*/
module "todo_app" {
  source = "./todo-app"

  environment_name = var.environment_name
  branch_name      = var.branch_name
  // branch.dev.tinakori.dev OR tinakori.dev
  frontend_url     = var.frontend_url
  docker_image_tag = var.docker_image_tag
  db_subnet_group  = var.db_subnet_group
}

locals {
  api_url = "api.${module.todo_app.frontend_url}"
}


# Export Terraform variable values to an Ansible var_file
resource "local_file" "tf_ansible_vars_file_new" {
  content  = <<-DOC
    # Ansible vars_file containing variable values from Terraform.
    # Generated by Terraform todo_app configuration.

    secretsmanager_secret_name: ${module.todo_app.db_todo_user_secretsmanager_name}
    secretsmanager_root_secret_name: ${module.todo_app.db_root_user_secretsmanager_name}
    rds_endpoint: ${module.todo_app.rds_endpoint}
    frontend_url: ${module.todo_app.frontend_url}
    backend_api_url: ${local.api_url}
    rds_root_user: ${module.todo_app.rds_root_user}
    s3_bucket_name: ${module.todo_app.s3_bucket_name}
    cloudfront_dist_id: ${module.todo_app.cloudfront_dist_id}
    DOC
  filename = "./tf_ansible_vars.yaml"
}
