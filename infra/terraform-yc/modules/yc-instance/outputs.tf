output "internal_ips" {
  value = { for idx, vm in yandex_compute_instance.vm-instance : var.vm_names[idx] => vm.network_interface.0.ip_address }
}