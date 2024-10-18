module "yc-network" {
  source       = "./modules/yc-network"
  zone         = var.zone
}

module "yc-instance" {
  source              = "./modules/yc-instance"
  platform_id         = var.platform_id
  zone                = var.zone
  private_subnet_id   = module.yc-network.private_subnet.id
  security_group_ids = [module.yc-network.nat-instance-sg.id]
  ssh_key_path        = var.ssh_key_path
}

module "yc-nat" {
  source             = "./modules/yc-nat"
  platform_id        = var.platform_id
  zone               = var.zone
  public_subnet_id   = module.yc-network.public_subnet.id
  security_group_ids = [module.yc-network.nat-instance-sg.id]
  network_id         = module.yc-network.network.id
  ssh_key_path       = var.ssh_key_path
}
