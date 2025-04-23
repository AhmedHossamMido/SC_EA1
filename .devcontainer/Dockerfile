# syntax=docker/dockerfile:1
FROM quay.io/jupyter/base-notebook:lab-4.3.6 AS base_image

# Installiere curl und andere benötigte Pakete
USER root
RUN apt-get update && apt-get install -y curl git build-essential && apt-get clean

# Installiere Miniconda und eine neue Umgebung mit Python 3.8
RUN curl -sSLo miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash miniconda.sh -b -u -p /opt/conda && \
    rm miniconda.sh && \
    /opt/conda/bin/conda create -n python38 python=3.8 && \
    /opt/conda/bin/conda clean -a -y

# Setze Miniconda in PATH
ENV PATH="/opt/conda/bin:$PATH"

# Setze Umgebungsvariablen
ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

# Wechsel zu Nutzer jovyan
USER $NB_USER

# Aktiviere conda als die Shell-Umgebung
SHELL ["conda", "run", "--no-capture-output", "-n", "python38", "/bin/bash", "-c"]

# Installiere uv als schnelle Alternative zu pip
RUN pip install uv==0.6.6

# Kopiere die requirements.txt und installiere alle Abhängigkeiten
COPY requirements.txt /tmp/requirements.txt
RUN mkdir -p $HOME/.cache && \
    uv pip install -r /tmp/requirements.txt && \
    python -m pyflyby.install_in_ipython_config_file

# Installiere ipykernel für die Jupyter-Integration
RUN pip install ipykernel

# Installiere den 'scipro' Kernel in Jupyter
RUN python -m ipykernel install --user --name scipro --display-name "SciPro Jupyter (Docker)"

# Setze den Arbeitsordner
WORKDIR /workspaces/SC_EA1_bis_EA3

# Setze JupyterHub Dienstpräfix
ENV JUPYTERHUB_SERVICE_PREFIX="/"
