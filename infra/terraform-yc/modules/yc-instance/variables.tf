variable "zone" {
  type = string
}

variable "platform_id" {
  type = string
}

variable "security_group_ids" {
  type = list(string)
}

variable "private_subnet_id" {
  type        = string
}

variable "ssh_key_path" {
  type = string
}

variable "vm_names" {
  type        = list(string)
  default     = ["test1", "test2", "test3"]
}

locals {
    vm_user          = "ubuntu"
}