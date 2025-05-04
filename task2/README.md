# DevOps Task 2

## Описание

В этом репозитории представлен пример инфраструктуры для автоматизированной установки Docker с помощью Ansible и тестирования HTTP-ответов с помощью Python-скрипта.

## Структура проекта

- `01_script/` — Python-скрипт и зависимости для проверки HTTP-статусов.
- `02_docker/` — Dockerfile для контейнеризации Python-скрипта.
- `03_ansible/` — Ansible-инфраструктура: playbook, инвентарь, роль, vault и конфиг.

## Быстрый старт

### 1. Установка Python-зависимостей

Перейдите в директорию со скриптом и установите зависимости:

```bash
cd 01_script
pip install -r requirements.txt
```

### 2. Запуск Python-скрипта

```bash
python3 main.py
```

### 3. Сборка и запуск Docker-контейнера

```bash
cd ../02_docker
docker build -t py_request .
docker run --rm py_request
```

### 4. Установка Docker на сервер с помощью Ansible

1. Перейдите в директорию Ansible:

    ```bash
    cd ../03_ansible
    ```

2. Убедитесь, что заполнены переменные в `vault.yml` (например, пароль пользователя).

3. Установите роль (если требуется):

    ```bash
    ansible-galaxy install -r requirements.yml -f
    ```

4. Запустите playbook:

    ```bash
    ansible-playbook playbook.yml --ask-become-pass
    ```

## Файлы и директории

- `main.py` — основной Python-скрипт для тестирования HTTP-ответов.
- `requirements.txt` — зависимости Python.
- `Dockerfile` — сборка контейнера для скрипта.
- `playbook.yml` — основной Ansible playbook.
- `Alvald1.docker_role/` — роль для установки Docker ([github.com/Alvald1/docker_role](https://github.com/Alvald1/docker_role)).
- `inventory.ini`, `ansible.cfg` — пример инвентаря и конфигурации Ansible.
- `vault.yml` — зашифрованные переменные (например, пароль пользователя).

## Примечания

- Для работы Ansible потребуется пароль пользователя (или настройка vault).
- Все переменные роли описаны в `Alvald1.docker_role/vars/main.yml`.
- Для запуска playbook требуется доступ к целевому хосту (см. `inventory.ini`).
