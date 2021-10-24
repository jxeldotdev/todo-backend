/* Environment and domain related variables */
// ci-and-infrastructure.dev.tinakori.dev
// tinakori.dev
variable "frontend_url" {
  type        = string
}


variable "hosted_zone_id" {
  type        = string
  description = "Route53 Hosted Zone ID - Used by Frontend module"
}

// api.ci-and-infrastructure.dev.tinakori.dev
// PROD: api.tinakori.dev

variable "branch_name" {
  type        = string
  description = "Name of git branch"
}

variable "environment" {
  type        = string
  default     = "development"
  description = "Name of environment. Possible values: development, production"

  validation {
    condition     = regex("development|production", var.environment)
    error_message = "Environment must be development or production."
  }
}

/* Database Variables */

variable "db_name" {
  type        = string
  default     = "todo"
  description = "Name of database that will be created in the RDS instance."
}

variable "master_db_user" {
  type        = string
  default     = "rdsmaster"
  description = "Name of Master Database User"
}

variable "db_instance_class" {
  type        = string
  default     = "db.t3.micro"
  description = "AWS RDS Instance Class for Database."
}

variable "db_subnet_group" {
  type        = string
  description = "Name of DB Subnet group to create RDS Instance in."
}

variable "backup_retention_period" {
  type        = number
  default     = 7
  description = "Database backup retention period in days"
}
