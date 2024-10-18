resource "yandex_compute_image" "ubuntu-1804-lts" {
  source_family = "ubuntu-1804-lts"
}

resource "yandex_compute_disk" "boot-disk-ubuntu" {
  count  = length(var.vm_names)
  name   = "${var.vm_names[count.index]}-boot-disk"
  type     = "network-hdd"
  zone     = var.zone
  size     = "20"
  image_id = yandex_compute_image.ubuntu-1804-lts.id
}

resource "yandex_compute_instance" "test-vm" {
  count       = length(var.vm_names)
  name        = var.vm_names[count.index]
  platform_id = var.platform_id
  zone        = var.zone

  resources {
    core_fraction = 20
    cores         = 2
    memory        = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-ubuntu[count.index].id
  }

  network_interface {
    subnet_id          = var.private_subnet_id
    security_group_ids = var.security_group_ids
  }

  metadata = {
    user-data = "#cloud-config\nusers:\n  - name: ${local.vm_user}\n    groups: sudo\n    shell: /bin/bash\n    sudo: 'ALL=(ALL) NOPASSWD:ALL'\n    ssh_authorized_keys:\n      - ${file(var.ssh_key_path)}"
  }
}