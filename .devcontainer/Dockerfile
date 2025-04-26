# Benutze das offizielle Jupyter-Base-Image als Ausgangspunkt
# Das jupyter/base-notebook ist ein vorgefertigtes Docker-Image, das Jupyter-Notebooks und grundlegende Python-Abhängigkeiten enthält.
# Es stellt sicher, dass du eine voll funktionsfähige Jupyter-Umgebung hast, die du anpassen kannst.
FROM jupyter/base-notebook:latest

# Installiere zusätzliche Pakete, die für den Container benötigt werden
# Wir wechseln hier zu 'root', um Systempakete zu installieren. Danach wechseln wir zurück zum Standardbenutzer 'nbuser'.
USER root

# Installiere Git
RUN apt-get update && apt-get install -y --no-install-recommends git

# Bereinige Paketlisten (für schlankeres Image)
RUN rm -rf /var/lib/apt/lists/*

# Wechsel zurück zum Standardbenutzer von Jupyter, der "nbuser" heißt
# Dies verhindert, dass während des Betriebs des Containers Sicherheitsprobleme auftreten, da root-Rechte nicht mehr benötigt werden.
USER $NB_USER

# Kopiere die requirements.txt in den Container, damit wir die benötigten Python-Abhängigkeiten installieren können
COPY .devcontainer/requirements.txt /tmp/requirements.txt

# Erstelle einen Ordner für die IPython Startup-Skripte
# Jupyter-Notebooks führen automatisch alle Python-Importe aus, die in den Startup-Dateien enthalten sind.
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
# Dies sorgt dafür, dass beim Starten von Jupyter-Notebooks alle genannten Bibliotheken automatisch importiert werden

# Installiere die Python-Abhängigkeiten aus der requirements.txt
# Hier werden alle Python-Pakete installiert, die du für dein Projekt benötigst.
RUN pip install -r /tmp/requirements.txt

# Installiere pyflyby, um die gewünschte Funktionalität sicherzustellen
# Dies wird benötigt, um die pyflyby-Erweiterung für Jupyter zu installieren und zu konfigurieren.
# Konfiguriere IPython automatisch
# RUN python3 -c "import pyflyby; pyflyby.install_in_ipython_config_file()"

# Diese Zeile sorgt dafür, dass pyflyby korrekt in die IPython-Konfiguration integriert wird, 
# was notwendig ist, um die automatische Importfunktion von pyflyby zu ermöglichen.

# Diese Zeile sorgt dafür, dass beim Starten von Jupyter Notebooks im Container keine Warnungen von pyflyby angezeigt werden
RUN echo "import warnings\nwarnings.filterwarnings('ignore', category=UserWarning, module='pyflyby')" > /home/$NB_USER/.ipython/profile_default/startup/01-ignore-pyflyby-warnings.py

# Standard-Startbefehl: Starte JupyterLab auf allen Schnittstellen (IP 0.0.0.0) und Port 8888
# --ip=0.0.0.0 stellt sicher, dass Jupyter von allen IPs im Container erreichbar ist.
# --port=8888 legt den Port fest, auf dem der Jupyter-Dienst läuft.
# --no-browser verhindert, dass Jupyter automatisch einen neuen Browser öffnet (nützlich in einem Docker-Container).
# --NotebookApp.token='' deaktiviert das Token, sodass du dich nicht mit einem Passwort anmelden musst.
# --NotebookApp.notebook_dir=/workspaces/SC_EA1_bis_EA3 legt das Verzeichnis fest, das als Arbeitsverzeichnis dient.
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.notebook_dir=/workspaces/SC_EA1_bis_EA3"]
