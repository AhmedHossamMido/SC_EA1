# syntax=docker/dockerfile:1

FROM quay.io/jupyter/base-notebook:lab-4.3.6 AS base_image

USER root
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache && \
    apt-get update && apt-get install -yq --no-install-recommends \
      debuginfod && \
      apt-get clean

ENV DEBUGINFOD_URLS="https://debuginfod.ubuntu.com/"

USER $NB_USER

SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

RUN pip install uv==0.6.6

COPY requirements.txt /tmp/requirements.txt
RUN mkdir -p $HOME/.cache
RUN --mount=type=cache,uid=$NB_UID,mode=7777,target=$HOME/.cache/uv \
    uv pip install -r /tmp/requirements.txt && \
    py pyflyby.install_in_ipython_config_file

ENV JUPYTERHUB_SERVICE_PREFIX="/"

# Standardverzeichnis in Codespace und Jupyter
WORKDIR /workspaces/SC_EA1_bis_EA3

# Starte JupyterLab automatisch beim Start
# CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]

RUN python -m ipykernel install --user --name scipro --display-name "SciPro Jupyter"
