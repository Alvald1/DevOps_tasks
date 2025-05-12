# YADRO Impulse 2025

## Структура репозитория

- `task1/` — базовые задания по Linux, bash и Docker.
- `task2/` — пример автоматизации установки Docker через Ansible и тестирования HTTP-ответов Python-скриптом.

## Быстрый старт

### Bash и Docker

В директории `task1` находятся примеры команд, bash-скриптов и Dockerfile. Для запуска скриптов:

```bash
cd task1
bash <имя_скрипта>.sh
```

### Python-скрипт для HTTP-запросов

В директории `task2/01_script`:

```bash
cd task2/01_script
pip install -r requirements.txt
python3 main.py
```

### Сборка и запуск Docker-контейнера

```bash
cd task2/02_docker
docker build -t py_request .
docker run --rm py_request
```

### Автоматизация с помощью Ansible

В директории `task2/03_ansible`:

```bash
cd task2/03_ansible
ansible-playbook playbook.yml --ask-become-pass
```

## Примечания

- Для работы с Ansible потребуется доступ к целевому серверу и корректно настроенный инвентарь.
- Все примеры предназначены для учебных целей и могут быть доработаны под ваши задачи.
