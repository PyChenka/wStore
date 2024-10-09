output "instance_internal_ip" {
  description = "Internal IP"
  value       = module.instance.ip_address
  sensitive   = true
}

output "instance_external_ip" {
  description = "External IP"
  value       = module.instance.nat_ip_address
}