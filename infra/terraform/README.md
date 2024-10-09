# Terraform Yandex Cloud Module

## Описание

Этот корневой модуль Terraform разворачивает инфраструктуру в Yandex Cloud, состоящую из сети (VPC) и экземпляра виртуальной машины (VM). Модуль использует провайдер `yandex` для взаимодействия с API Yandex Cloud и поддерживает управление состоянием через бэкенд на S3.

## Зависимости

- Terraform >= 0.13
- Провайдер Yandex Cloud `yandex-cloud/yandex` версии 0.97.0
- Доступ к Yandex Object Storage для хранения состояния

