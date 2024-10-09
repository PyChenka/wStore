output "instance_internal_ips_by_name" {
  description = "Internal IPs for each instance by name"
  value       = module.instance.internal_ips
  sensitive   = true
}

output "instance_external_ips_by_name" {
  description = "External IPs for each instance by name"
  value       = module.instance.external_ips
}
