# Benutze das offizielle Jupyter-Base-Image als Ausgangspunkt
FROM jupyter/base-notebook:latest

# Installiere zusätzliche Pakete als root (erforderlich für Systempakete)
USER root
# Dieser Befehl installiert das Paket 'git' und führt eine Bereinigung der Paketlisten durch, um das Docker-Image kleiner zu machen
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && \
    rm -rf /var/lib/apt/lists/*  # Entfernt die temporären Paketlisten, um das Image kleiner zu halten

# Wechsel zurück zum Standard-Jupyter-Benutzer
USER $NB_USER
# $NB_USER ist die Umgebungsvariable, die auf den standardmäßigen Benutzer von Jupyter (in der Regel 'jovyan') verweist.

# Kopiere die 'requirements.txt' Datei vom lokalen Projektordner in das Container-Dateisystem
COPY .devcontainer/requirements.txt /tmp/requirements.txt
# Hier wird die Datei 'requirements.txt', die alle erforderlichen Python-Pakete listet, ins temporäre Verzeichnis '/tmp' im Container kopiert.
# Dieser Schritt ist notwendig, um die Pakete aus dieser Datei im nächsten Schritt zu installieren.

# Installiere die Python-Pakete aus der requirements.txt
RUN pip install -r /tmp/requirements.txt
# Der Befehl 'pip install -r /tmp/requirements.txt' installiert alle Python-Pakete, die in der 'requirements.txt' aufgelistet sind.
# Die 'requirements.txt' enthält normalerweise Bibliotheken, die für dein Projekt erforderlich sind, wie z.B. 'pandas', 'numpy', etc.

# Der Standard-Startbefehl für den Container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.notebook_dir=/workspaces/SC_EA1_bis_EA3"]
# Dieser Befehl startet den JupyterLab-Server, wenn der Container ausgeführt wird.
# Erklärung der Optionen:
# --ip=0.0.0.0: Jupyter wird auf allen IP-Adressen des Containers lauschen, sodass es von außen zugänglich ist.
# --port=8888: Der JupyterLab-Server wird auf Port 8888 laufen.
# --no-browser: Verhindert, dass Jupyter automatisch einen Browser öffnet.
# --NotebookApp.token='': Dies deaktiviert die Token-Authentifizierung für den Zugriff auf das JupyterLab. (Sicherstellen, dass nur autorisierte Benutzer auf den Container zugreifen.)
# --NotebookApp.notebook_dir=/workspaces/SC_EA1_bis_EA3: Legt das Verzeichnis fest, das als Arbeitsverzeichnis für JupyterLab verwendet wird. Alle Notebooks und Dateien in diesem Ordner werden angezeigt.

