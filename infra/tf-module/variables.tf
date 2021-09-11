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
  default     = "dev"
  description = "description"
}


/* Database Variables */


variable "db_name" {
  type        = string
  default     = "todo"
  description = "description"
}

variable "db_user" {
  type        = string
  default     = "app"
  description = "description"
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
