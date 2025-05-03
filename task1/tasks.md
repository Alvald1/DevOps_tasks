# DevOps задания

## 1. Команды для работы с файлами и выводом в Linux

- Печать строки "Hello, DevOps!":
  ```bash
  echo "\"Hello, DevOps!"
  ```

- Запись строки в файл `hello.txt` в домашней директории:
  ```bash
  echo "\"Hello, DevOps!" > ~/hello.txt
  ```

- Вывод содержимого файла на экран:
  ```bash
  cat ~/hello.txt
  ```

## 2. Поиск по логам

- Чтение `/var/log/syslog`:
  ```bash
  cat /var/log/syslog
  ```

- Поиск строк с "error" (или другим словом):
  ```bash
  grep -n /var/log/syslog -e "error"
  ```

- Вывод первых 5 совпавших строк:
  ```bash
  grep -n /var/log/syslog -e "error" | head -n 5
  ```

- Всё одной командой с использованием конвейеров (pipes):
  ```bash
  cat /var/log/syslog | grep -n -e "error" | head -n 5
  ```

## 3. Bash-скрипт для поиска слова в файле

Создайте файл и запишите туда нужные строки. Далее используйте скрипт для поиска слова (например, `path`) в этом файле:

```bash
#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Ошибка: не задано слово и файл для поиска."
  echo "Использование: $0 <слово> <файл>"
  exit 1
fi

if [ ! -f "$2" ]; then
  echo "Ошибка: файл '$2' не найден."
  exit 2
fi

grep -e "$1" "$2"
```

## 4. Пример Dockerfile

```Dockerfile
FROM ubuntu:latest 

RUN apt-get update && \
    apt-get install -y wget python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*
    
COPY search_path.sh extract_path_value.py config.txt /tmp/

RUN chmod +x /tmp/search_path.sh /tmp/extract_path_value.py
```