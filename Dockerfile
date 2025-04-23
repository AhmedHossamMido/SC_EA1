# syntax=docker/dockerfile:1

# Basis: JupyterLab mit Python
FROM quay.io/jupyter/base-notebook:lab-4.3.6 AS base_image

# Systempakete installieren
USER root
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache && \
    apt-get update && apt-get install -yq --no-install-recommends \
      debuginfod && \
      if [ "$(dpkg --print-architecture)" != "amd64" ]; then apt-get install -yq --no-install-recommends build-essential; fi && \
    apt-get clean

ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

# Zurück zu user jovyan
USER $NB_USER

# Aktiviere conda shell
SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

# Schnellerer pip-Ersatz
RUN pip install uv==0.6.6

# requirements.txt kopieren
COPY requirements.txt /tmp/requirements.txt

# Cache-Verzeichnis erstellen
RUN mkdir -p $HOME/.cache

# Python-Abhängigkeiten installieren
RUN --mount=type=cache,uid=$NB_UID,mode=7777,target=$HOME/.cache/uv \
    uv pip install -r /tmp/requirements.txt && \
    py pyflyby.install_in_ipython_config_file

# Fix für jupyter-marimo-proxy
ENV JUPYTERHUB_SERVICE_PREFIX="/"

# Optional: Arbeitsverzeichnis setzen (nicht kritisch für Codespaces)
WORKDIR /home/jovyan
