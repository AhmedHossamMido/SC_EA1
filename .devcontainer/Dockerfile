# Basierend auf dem offiziellen Jupyter-Image
FROM jupyter/base-notebook:lab-4.3.6

# Setze den Benutzer auf jovyan (wird standardmäßig vom jupyter/base-notebook-Image verwendet)
USER root

# Installiere alle Systemabhängigkeiten, falls nötig
RUN apt-get update && apt-get install -y --no-install-recommends \
    debuginfod build-essential

# Wechsle zu jovyan-Benutzer
USER $NB_USER

# Installiere Python-Pakete aus requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Teste die Installation von pyflyby
RUN python -c "import pyflyby; print('pyflyby version:', pyflyby.__version__)"

# Installiere pyflyby in der IPython-Konfiguration
RUN python -m pyflyby.install_in_ipython_config_file

# Setze den Arbeitsordner (optional)
WORKDIR /home/jovyan

# Exponiere den Port für JupyterLab (normalerweise 8888)
EXPOSE 8888

# Starte JupyterLab
CMD ["start-notebook.sh"]
