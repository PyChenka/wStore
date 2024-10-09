resource "yandex_compute_instance" "vm-service" {
    count = length(var.vm_names)
    name  = var.vm_names[count.index]
    platform_id = var.platform_id

    scheduling_policy {
        preemptible = var.scheduling_policy
    }

    resources {
        cores  = 2
        memory = 2
    }

    boot_disk {
        initialize_params {
            image_id = var.image_id
        }
    }

    network_interface {
        subnet_id = var.subnet_id
        nat       = true
    }

    metadata = {
        ssh-keys = "ubuntu:${var.ssh_public_key}"
    }
}
