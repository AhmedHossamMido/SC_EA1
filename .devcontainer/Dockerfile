# Verwende das neueste Jupyter-Base-Notebook-Image
FROM jupyter/base-notebook:latest

# Installiere alle Systemabhängigkeiten
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    debuginfod build-essential && \
    rm -rf /var/lib/apt/lists/*

# Wechsle zu jovyan (Standardbenutzer von Jupyter)
USER $NB_USER

# Kopiere die requirements.txt und installiere Python-Pakete
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Starte JupyterLab
CMD ["start-notebook.sh"]
