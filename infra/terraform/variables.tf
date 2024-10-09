variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
}

variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
}

variable "zone" {
  description = "Instance Zone"
  type        = string
  default     = "ru-central1-a"
}

variable "platform_id" {
  description = "Instance Platform ID"
  type        = string
}

variable "network_zones" {
  description = "Instance Network Zones"
  type        = set(string)
}

variable "image_id" {
  description = "Yandex Cloud Image ID"
  type        = string
  default     = "fd80qm01ah03dkqb14lc"
}

variable "scheduling_policy" {
  description = "Instance Scheduling Policy"
  type        = bool
  default     = true
}

variable "ssh_public_key" {
  description = "SSH public key for instance access"
  type        = string
}

variable "vm_names" {
  description = "List of the resource group names"
  type        = list(string)
  default     = ["wstore-service", "wstore-test", "wstore-prod"]
}