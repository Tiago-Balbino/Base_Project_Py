FROM python:3.12-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]
