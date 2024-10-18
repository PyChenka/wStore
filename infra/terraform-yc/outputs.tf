output "instance_internal_ips_by_name" {
  description = "Internal IPs for each VM by name"
  value       = module.yc-instance.internal_ips
  sensitive   = true
}

output "nat_external_ip" {
  description = "NAT-instance external IP"
  value       = module.yc-nat.nat_instance_external_ip
}

output "nat_internal_ip" {
  description = "NAT-instance internal IP"
  value       = module.yc-nat.nat_instance_internal_ip
  sensitive   = true
}
