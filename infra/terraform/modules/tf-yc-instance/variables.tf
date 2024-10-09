variable "platform_id" {
  description = "Instance Platform ID"
  type        = string
}

variable "scheduling_policy" {
  description = "Instance Scheduling Policy"
  type        = bool
  default     = true
}

variable "image_id" {
  description = "Yandex Cloud Image ID"
  type        = string
  default     = "fd80qm01ah03dkqb14lc"
}

variable "subnet_id" {
  description = "Yandex Cloud Subnet ID"
  type        = string
}

variable "ssh_public_key" {
  description = "SSH public key for instance access"
  type        = string
}
