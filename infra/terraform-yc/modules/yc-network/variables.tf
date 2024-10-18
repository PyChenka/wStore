variable "zone" {
  type = string
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

locals {
  sg_nat_name         = "nat-instance-sg"
}