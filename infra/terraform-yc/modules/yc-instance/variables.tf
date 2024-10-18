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
  type = string
}

variable "vm_ssh_key_path" {
  type = list(string)
}

variable "vm_names" {
  type = list(string)
}

variable "vm_static_ips" {
  type    = list(string)
}


locals {
  vm_user = "ubuntu"
}