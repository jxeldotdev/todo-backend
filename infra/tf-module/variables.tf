/* Environment and domain related variables */
variable "frontend_domain_prefix" {
  type        = string
  default     = "${var.branch_name}-${var.environment}.todo"
  description = "description"
}

variable "backend_domain_prefix" {
  type = string
  default = "api.${var.branch_name}-${var.environment}.todo"
}

variable "branch_name" {
  type        = string
  description = "Name of git branch"
}

variable "environment" {
  type        = string
  default     = "development"
  description = "Name of environment. Possible values: development, production"
}

/* Database Variables */

variable "db_name" {
  type        = string
  default     = "todo"
  description = "Name of database that will be created in the RDS instance."
}

variable "master_db_user" {
  type        = string
  default     = "master"
  description = "Name of Master Database User"
}

variable "db_instance_class" {
  type        = string
  default     = "db.t3.micro"
  description = "AWS RDS Instance Class for Database."
}

variable "db_monitoring_role_name" {
  type        = string
  default     = ""
  description = "description"
}

variable "backup_retention_period" {
  type        = string
  default     = "7"
  description = "description"
}
