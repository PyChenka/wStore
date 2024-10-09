# Terraform YC Module: tf-yc-network

## Описание

Модуль `tf-yc-network` предназначен для работы с сетевыми ресурсами в Yandex Cloud. Он использует ресурсы `yandex_vpc_network` и `yandex_vpc_subnet` для получения информации о сетевых сущностях в облаке Yandex Cloud.

## Зависимости

Этот модуль зависит от провайдера Yandex Cloud версии 0.97.0.

## Параметры

### Переменные

- **network_zones**
  - Описание: Список зон, которые используются для создания подсетей
  - Тип: `set(string)`
  
### Outputs

- **vpc_network_id**
  - Описание: ID сети VPC
  - Тип: `string`
  
- **vpc_subnet_ids**
  - Описание: Карта, содержащая ID подсетей VPC в каждой зоне
  - Тип: `map(string)`
