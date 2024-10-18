variable "platform_id" {
  type = string
}

variable "zone" {
  type = string
}

variable "public_subnet_id" {
  type = string
}

variable "security_group_ids" {
  type = list(string)
}

variable "network_id" {
  type = string
}

variable "ssh_key_path" {
  type = string
}

locals {
  vm_nat_name = "nat-instance"
  vm_nat_user = "ubuntu"
}