# syntax=docker/dockerfile:1
FROM quay.io/jupyter/base-notebook:lab-4.3.6 AS base_image

# Installiere benötigte Pakete
USER root
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache && \
    apt-get update && \
    apt-get install -yq --no-install-recommends \
    debuginfod git build-essential && \
    apt-get clean

# Setze Umgebungsvariablen
ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

# Wechsel zu Nutzer jovyan
USER $NB_USER

# Aktiviere conda als die Shell-Umgebung
SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

# Installiere Python 3.8 explizit
RUN conda install python=3.8

# Installiere uv als schnelle Alternative zu pip
RUN pip install uv==0.6.6

# Kopiere die requirements.txt und installiere alle Abhängigkeiten
COPY requirements.txt /tmp/requirements.txt
RUN mkdir -p $HOME/.cache && \
    uv pip install -r /tmp/requirements.txt && \
    py pyflyby.install_in_ipython_config_file

# Installiere ipykernel für die Jupyter-Integration
RUN conda install -c conda-forge ipykernel

# Installiere den 'scipro' Kernel in Jupyter
RUN conda run -n base python -m ipykernel install --user --name scipro --display-name "SciPro Jupyter (Docker)"

# Setze den Arbeitsordner
WORKDIR /workspaces/SC_EA1_bis_EA3

# Setze JupyterHub Dienstpräfix
ENV JUPYTERHUB_SERVICE_PREFIX="/"
