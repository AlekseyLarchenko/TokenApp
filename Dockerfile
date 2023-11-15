FROM debian:bullseye-slim

ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libffi-dev \
        libssl-dev \
        libxml2-dev \
        xmlsec1 \
        python3-pip \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./ .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]

