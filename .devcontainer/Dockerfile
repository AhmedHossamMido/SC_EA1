# Verwende das Jupyter-Base-Notebook-Image als Basis
FROM quay.io/jupyter/base-notebook:lab-4.3.6

# Setze den Benutzer auf root, um Systempakete zu installieren
USER root

# Entferne die APT-Cache-Konfiguration und sorge dafür, dass Pakete nicht unnötig zwischengespeichert werden
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

# Installiere notwendige Systempakete und Abhängigkeiten
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  apt-get update && apt-get install -yq --no-install-recommends \
    debuginfod \
    build-essential && \
  rm -rf /var/lib/apt/lists/*

# Setze Umgebungsvariablen für den debuginfod-Server
ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

# Installiere Python- und Jupyter-Pakete, sowie Abhängigkeiten
USER $NB_USER

# Versetze alle nachfolgenden Befehle in die Conda "base" Umgebung, um die Abhängigkeiten zu installieren
SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

# Erstelle das Cache-Verzeichnis für die pip-Cache-Dateien
RUN mkdir -p $HOME/.cache

# Installiere Python-Pakete mit pip (entspricht dem Kurstext-Dockerfile)
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

# Fix für das Jupyter-Marimo-Proxy
ENV JUPYTERHUB_SERVICE_PREFIX="/"

# Exponiere den Port für JupyterLab (8888) und optional den für Viztracer (9001)
EXPOSE 8888
EXPOSE 9001

# Stelle sicher, dass beim Start des Containers JupyterLab ausgeführt wird
CMD ["start-notebook.sh"]
