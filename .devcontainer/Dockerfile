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

# We need to set conda as the environment shell
SHELL ["conda", "run", "--no-capture-output", "-n", "base", "/bin/bash", "-c"]

# Install uv and packages
RUN pip install uv==0.6.6

# Copy the requirements file and install the dependencies
COPY requirements.txt /tmp/requirements.txt
RUN mkdir -p $HOME/.cache
RUN --mount=type=cache,uid=$NB_UID,mode=7777,target=$HOME/.cache/uv \
    uv pip install -r /tmp/requirements.txt && \
    py pyflyby.install_in_ipython_config_file

# Install ipykernel (important to link with Jupyter)
RUN conda install -c conda-forge ipykernel

# Create a new kernel named 'scipro' based on the environment
RUN python -m ipykernel install --user --name scipro --display-name "SciPro Jupyter (Docker)"

ENV JUPYTERHUB_SERVICE_PREFIX="/"

# Default working directory in Codespace and Jupyter
WORKDIR /workspaces/SC_EA1_bis_EA3
