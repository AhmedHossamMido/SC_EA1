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

# Wechsel zu Nutzer jovyan
USER $NB_USER

# Setze den Arbeitsordner
WORKDIR /workspaces/SC_EA1_bis_EA3

# Installiere pip und pyflyby (sowie alle Abhängigkeiten aus requirements.txt)
# Wir stellen sicher, dass pip und pyflyby korrekt ohne Conda ausgeführt werden
RUN pip install --upgrade pip

# Kopiere die requirements.txt
COPY requirements.txt /tmp/requirements.txt

# Installiere alle Anforderungen und pyflyby
RUN pip install -r /tmp/requirements.txt && \
    # Überprüfe die Installation von pyflyby
    python -c "import pyflyby; print('pyflyby version:', pyflyby.__version__)" && \
    # Installiere pyflyby in die IPython-Konfiguration
    python -m pyflyby.install_in_ipython_config_file


# Installiere ipykernel für die Jupyter-Integration
RUN conda install -c conda-forge ipykernel

# Installiere den 'scipro' Kernel in Jupyter
RUN conda run -n python38 python -m ipykernel install --user --name scipro --display-name "SciPro Jupyter (Docker)"

# Setze JupyterHub Dienstpräfix
ENV JUPYTERHUB_SERVICE_PREFIX="/"
