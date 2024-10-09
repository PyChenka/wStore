module "instance" {
    source = "./modules/tf-yc-instance"

    subnet_id = module.network.vpc_subnet_ids[var.zone]
    platform_id = var.platform_id
    ssh_public_key = var.ssh_public_key
}

module "network" {
    source = "./modules/tf-yc-network"
    network_zones = var.network_zones
}