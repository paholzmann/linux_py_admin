FROM debian:12

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3 pip \
    && apt-get clean

WORKDIR /app

COPY requirements.txt

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ..