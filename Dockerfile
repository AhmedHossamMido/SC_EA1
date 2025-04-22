# syntax=docker/dockerfile:1

FROM quay.io/jupyter/base-notebook:lab-4.3.6 AS base_image

USER root

# APT-Caching und Git installieren
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -yq --no-install-recommends \
      git \
      debuginfod \
      # optional: Build-Werkzeuge für Scalene auf Nicht-AMD64-Architektur
      && if [ "$(dpkg --print-architecture)" != "amd64" ]; then apt-get install -yq build-essential; fi \
    && rm -rf /var/lib/apt/lists/*
    
ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

# Zurück zum User jovyan (Standard bei Jupyter)
USER $NB_USER

# Conda Shell aktivieren für weitere Befehle
SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

# uv installieren (schneller als pip)
RUN pip install uv==0.6.6

# Cache-Ordner für Python-Pakete erstellen
RUN mkdir -p $HOME/.cache

# Python-Abhängigkeiten installieren
RUN --mount=type=cache,uid=$NB_UID,mode=7777,target=$HOME/.cache/uv \
  uv pip install \
    marimo==0.11.20 \
    jupyter-marimo-proxy==0.0.4 \
    jupyterlab-pyflyby==5.1.2 \
    pyflyby==1.9.11 \
    altair==5.5.0 \
    hvplot==0.11.2 \
    matplotlib==3.10.1 \
    memray==1.16.0 \
    numba==0.61.0 \
    numpy \
    pandas==2.2.3 \
    plotly==6.0.0 \
    polars==1.25.2 \
    pyarrow==19.0.1 \
    scalene==1.5.51 \
    scipy==1.15.2 \
    viztracer==1.0.3 && \
  py pyflyby.install_in_ipython_config_file

# JupyterLab benötigt diese Variable für Marimo
ENV JUPYTERHUB_SERVICE_PREFIX="/"
