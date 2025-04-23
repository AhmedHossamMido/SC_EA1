# syntax=docker/dockerfile:1
FROM quay.io/jupyter/base-notebook:lab-4.3.6 AS base_image

# Installiere benötigte Pakete
USER root
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache && \
    apt-get update && \
    apt-get install -yq --no-install-recommends \
    debuginfod git build-essential libomp-dev && \
    apt-get clean

# Setze Umgebungsvariablen
ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

# Wechsel zu Nutzer jovyan
USER $NB_USER

# Installiere Miniconda und eine neue Umgebung mit Python 3.8
RUN curl -sSLo miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash miniconda.sh -b -u -p /opt/conda && \
    rm miniconda.sh && \
    /opt/conda/bin/conda create -n python38 python=3.8 && \
    /opt/conda/bin/conda clean -a -y

# Setze Conda-Binärpfad und die Umgebung
ENV PATH=/opt/conda/bin:$PATH
ENV CONDA_DEFAULT_ENV=python38

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
RUN conda run -n python38 python -m ipykernel install --user --name scipro --display-name "SciPro Jupyter (Docker)"

# Setze den Arbeitsordner
WORKDIR /workspaces/SC_EA1_bis_EA3

# Setze JupyterHub Dienstpräfix
ENV JUPYTERHUB_SERVICE_PREFIX="/"
