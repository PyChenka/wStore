data "yandex_vpc_network" "ws-network" {
  name = "ws-network"
}

data "yandex_vpc_subnet" "ws-subnet" {
  for_each = var.network_zones
  name = "${data.yandex_vpc_network.ws-network.name}-${each.key}"
}
