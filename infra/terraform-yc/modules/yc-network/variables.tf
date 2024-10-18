variable "zone" {
  type = string
}

locals {
  network_name     = "ws-network"
  subnet_name1     = "ws-public-subnet"
  subnet_name2     = "ws-private-subnet"
  sg_nat_name      = "nat-instance-sg"
}