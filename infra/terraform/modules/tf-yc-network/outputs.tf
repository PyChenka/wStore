output "vpc_network_id" {
  value = data.yandex_vpc_network.ws-network.id
}

output "vpc_subnet_ids" {
  value = { for zone, subnet in data.yandex_vpc_subnet.ws-subnet : zone => subnet.id }
}