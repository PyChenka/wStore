module "yc-network" {
  source       = "./modules/yc-network"
  zone         = var.zone
  network_name = var.network_name
  public_subnet_name = var.public_subnet_name
  private_subnet_name = var.private_subnet_name
}

module "yc-instance" {
  source              = "./modules/yc-instance"
  platform_id         = var.platform_id
  zone                = var.zone
  private_subnet_id   = module.yc-network.private_subnet.id
  security_group_ids  = [module.yc-network.nat-instance-sg.id]
  vm_names            = var.vm_names
  vm_ssh_key_path     = var.vm_ssh_key_path
  vm_static_ips          = var.vm_static_ips
}

module "yc-nat" {
  source              = "./modules/yc-nat"
  platform_id         = var.platform_id
  zone                = var.zone
  public_subnet_id    = module.yc-network.public_subnet.id
  security_group_ids  = [module.yc-network.nat-instance-sg.id]
  network_id          = module.yc-network.network.id
  vm_nat_ssh_key_path = var.vm_nat_ssh_key_path
}
