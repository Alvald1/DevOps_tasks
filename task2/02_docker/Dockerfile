FROM ubuntu:22.04

WORKDIR /app

RUN apt update && apt install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* 

COPY 01_script/requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY 01_script/main.py ./

CMD ["python3", "main.py"]
