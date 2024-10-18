variable "cloud_id" {
  type = string
}

variable "folder_id" {
  type = string
}

variable "zone" {
  type = string
}

variable "platform_id" {
  type = string
}

variable "vm_nat_ssh_key_path" {
  type = string
}

variable "vm_ssh_key_path" {
  type = list(string)
}

variable "vm_names" {
  type = list(string)
}

variable "vm_static_ips" {
  type = list(string)
}

variable "network_name" {
  type = string
}

variable "public_subnet_name" {
  type = string
}

variable "private_subnet_name" {
  type = string
}