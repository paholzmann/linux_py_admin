# Basis-Image
FROM debian:latest

# Um Interaktionen bei apt zu vermeiden
ENV DEBIAN_FRONTEND=noninteractive

# Update + Python3 + pip + venv installieren
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis im Container
WORKDIR /app

# requirements.txt ins Image kopieren
COPY requirements.txt .

# Virtuelle Umgebung erstellen und aktivieren, Pakete installieren
RUN python3 -m venv venv && \
    ./venv/bin/pip install --upgrade pip && \
    ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Standardbefehl beim Starten des Containers: virtuelle Umgebung aktivieren
CMD ["/bin/bash"]
