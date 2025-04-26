FROM jupyter/base-notebook:latest

# Installiere zusätzliche Pakete
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && \
    rm -rf /var/lib/apt/lists/*

# Wechsel zurück zum normalen User
USER $NB_USER

# Kopiere requirements.txt hinein!
COPY .devcontainer/requirements.txt /tmp/requirements.txt

# Installiere die Python-Pakete aus der requirements.txt-Datei
RUN pip install -r /tmp/requirements.txt

# Installiere pyflyby und führe die Konfiguration für IPython aus
# Diese Zeile stellt sicher, dass pyflyby korrekt in der IPython-Konfigurationsdatei installiert wird.
RUN pyflyby.install_in_ipython_config_file

# IPython Startup Imports automatisch erstellen
RUN mkdir -p /home/$NB_USER/.ipython/profile_default/startup && \
    printf "import marimo\n\
import pyflyby\n\
import altair as alt\n\
import hvplot\n\
import matplotlib.pyplot as plt\n\
import numba\n\
import numpy as np\n\
import pandas as pd\n\
import plotly.express as px\n\
import polars as pl\n\
import pyarrow\n\
import scipy\n" > /home/$NB_USER/.ipython/profile_default/startup/00-startup.py

# Hier fügen wir die Zeile ein, um die Warnung zu unterdrücken
RUN echo "import warnings\nwarnings.filterwarnings('ignore', category=UserWarning, module='pyflyby')" >> /home/$NB_USER/.ipython/profile_default/startup/00-startup.py

# Standard-Startbefehl: Starte Jupyter Notebook und öffne das Verzeichnis
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.notebook_dir=/workspaces/SC_EA1_bis_EA3"]
