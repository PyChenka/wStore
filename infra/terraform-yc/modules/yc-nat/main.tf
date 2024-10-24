resource "yandex_compute_image" "nat-instance-ubuntu" {
  source_family = "nat-instance-ubuntu"
}

resource "yandex_compute_disk" "boot-disk-nat" {
  name     = "boot-disk-nat"
  type     = "network-hdd"
  zone     = var.zone
  size     = "20"
  image_id = yandex_compute_image.nat-instance-ubuntu.id
}

resource "yandex_compute_instance" "nat_instance" {
  name        = local.vm_nat_name
  platform_id = var.platform_id
  zone        = var.zone

  resources {
    core_fraction = 20
    cores         = 2
    memory        = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-nat.id
  }

  network_interface {
    subnet_id          = var.public_subnet_id
    security_group_ids = var.security_group_ids
    nat                = true
  }

  metadata = {
    user-data = "#cloud-config\nusers:\n  - name: ${local.vm_nat_user}\n    groups: sudo\n    shell: /bin/bash\n    sudo: 'ALL=(ALL) NOPASSWD:ALL'\n    ssh_authorized_keys:\n      - ${file(var.vm_nat_ssh_key_path)}"
  }

  connection {
    type     = "ssh"
    user     = local.vm_nat_user
    private_key = file(var.vm_nat_ssh_key_path)
    host     = yandex_compute_instance.nat_instance.network_interface[0].nat_ip_address
  }
}

resource "yandex_vpc_route_table" "nat_route_table" {
  name       = "${local.vm_nat_name}-route"
  network_id = var.network_id

  static_route {
    destination_prefix = "0.0.0.0/0"
    next_hop_address   = yandex_compute_instance.nat_instance.network_interface[0].ip_address
  }
}

resource "null_resource" "nat_port_forwarding" {
  depends_on = [yandex_compute_instance.nat_instance]

  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      user        = local.vm_nat_user
      private_key = file(var.vm_nat_ssh_key_path)
      host        = yandex_compute_instance.nat_instance.network_interface[0].nat_ip_address
    }

    inline = [
      "sudo sysctl -w net.ipv4.ip_forward=1",

      "sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination 192.168.1.2:22",

      "sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j DNAT --to-destination 192.168.1.3:22",

      "sudo iptables -t nat -A PREROUTING -p tcp --dport 24 -j DNAT --to-destination 192.168.1.4:22",

      "sudo iptables-save"
    ]
  }
}
