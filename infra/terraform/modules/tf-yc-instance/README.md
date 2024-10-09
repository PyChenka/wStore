# Terraform YC Module: tf-yc-instance

## Описание

Модуль `tf-yc-instance` предназначен для развертывания виртуальных машин в Yandex Cloud. Он использует ресурс `yandex_compute_instance` для создания и настройки экземпляров виртуальных машин в облаке Yandex Cloud.

## Зависимости

Этот модуль зависит от провайдера Yandex Cloud версии 0.97.0.

## Параметры

### Переменные

- **platform_id**
  - Описание: ID платформы для создания экземпляра
  - Тип: `string`
- **scheduling_policy**
  - Описание: Политика планирования экземпляра (предоставление)
  - Тип: `bool`
  - Значение по умолчанию: `true`
- **image_id**
  - Описание: ID образа Yandex Cloud
  - Тип: `string`
  - Значение по умолчанию: `"fd80qm01ah03dkqb14lc"`
- **subnet_id**
  - Описание: ID подсети Yandex Cloud
  - Тип: `string`

### Outputs

- **ip_address**
  - Описание: Внутренний IP-адрес экземпляра
  - Тип: `string`
- **nat_ip_address**
  - Описание: Внешний IP-адрес экземпляра
  - Тип: `string`