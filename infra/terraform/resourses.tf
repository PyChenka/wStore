#resource "local_file" "inventory" {
#  content = templatefile("${path.module}/inventory.tpl", {
#    backend_ip  = module.instance.ip_address,
#    frontend_ip = module.instance.ip_address
#  })
#  filename = "${path.module}/../example-02/inventory/yandexcloud.yaml"
#}
