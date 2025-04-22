# Verwenden des offiziellen Python 3.8 Slim-Image als Basis
FROM python:3.8-slim

# Installieren der benötigten Systemabhangigkeiten (einschließlich git)
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Setze globale Git-Konfiguration für Rebase beim Pull
RUN git config --global pull.rebase true

# Arbeitsverzeichnis im Container festlegen
WORKDIR /workspace

# Kopiere requirements.txt ins Container-Dateisystem
COPY requirements.txt .

# Installiere die Python-Abhängigkeiten
RUN pip install -r requirements.txt

# Der Container läuft im /workspace-Verzeichnis
CMD ["bash"]
