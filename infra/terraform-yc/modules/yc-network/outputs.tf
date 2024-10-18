output "network" {
  value       = yandex_vpc_network.network
}

output "private_subnet" {
  value       = yandex_vpc_subnet.private_subnet
}

output "public_subnet" {
  value       = yandex_vpc_subnet.public_subnet
}

output "nat-instance-sg" {
  value       = yandex_vpc_security_group.nat-instance-sg
}
