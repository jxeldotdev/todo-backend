variable "branch_name" {
  type        = string
  description = "Branch name. Used by in tags and resource names."
}

variable "environment_name" {
  type        = string
  description = "Environment name. Used in tags and resource names."
}

variable "api_url" {
  type        = string
  description = "Desired backend API URL"
}

variable "frontend_url" {
  type        = string
  description = "Vue Frontend URL"
}
