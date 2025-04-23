# syntax=docker/dockerfile:1
# Verwende das jupyter base-notebook-Image
FROM quay.io/jupyter/base-notebook:lab-4.3.6 AS base_image

USER root

# Installiere debuginfod und git
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache && \
    apt-get update && \
    apt-get install -yq --no-install-recommends \
    debuginfod git build-essential && \
    apt-get clean

ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

# Wechsle zurück zu $NB_USER (standardmäßiger Benutzer)
USER $NB_USER

# Setze Conda als Standard-Shell
SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

# Erstelle eine neue Conda-Umgebung mit Python 3.8
RUN conda create --name scipro python=3.8 && \
    conda clean --all -y

# Installiere uv als fast alternative für pip
RUN pip install uv==0.6.6

# Kopiere die requirements.txt und installiere die Pakete
COPY requirements.txt /tmp/requirements.txt
RUN mkdir -p $HOME/.cache
RUN --mount=type=cache,uid=$NB_UID,mode=7777,target=$HOME/.cache/uv \
    uv pip install -r /tmp/requirements.txt && \
    py pyflyby.install_in_ipython_config_file

# Installiere ipykernel (damit Jupyter es erkennt)
RUN conda run -n scipro pip install ipykernel

# Erstelle einen neuen Jupyter-Kernel namens 'scipro'
RUN conda run -n scipro python -m ipykernel install --user --name scipro --display-name "SciPro Jupyter (Docker)"

# Setze JupyterHub Service Prefix
ENV JUPYTERHUB_SERVICE_PREFIX="/"

# Definiere das Arbeitsverzeichnis in GitHub Codespace und Jupyter
WORKDIR /workspaces/SC_EA1_bis_EA3

# Installiere zusätzliche Python-Pakete
RUN conda run -n scipro pip install \
    scalene==1.5.51 \
    memray==1.16.0 \
    numba==0.61.0 \
    numpy \
    pandas==2.2.3 \
    matplotlib==3.10.1 \
    plotly==6.0.0 \
    scipy==1.15.2 \
    altair==5.5.0 \
    hvplot==0.11.2 \
    jupyter-marimo-proxy==0.0.4 \
    marimo==0.11.20 \
    pyflyby==1.9.11 \
    jupyterlab-pyflyby==5.1.2

# Setze den JupyterHub Prefix
ENV JUPYTERHUB_SERVICE_PREFIX="/"
