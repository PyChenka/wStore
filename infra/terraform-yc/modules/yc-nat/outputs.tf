output "nat_instance_external_ip" {
  value = yandex_compute_instance.nat_instance.network_interface[0].nat_ip_address
}

output "nat_instance_internal_ip" {
  value = yandex_compute_instance.nat_instance.network_interface[0].ip_address
}
