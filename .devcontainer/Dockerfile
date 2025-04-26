# Beginne mit dem offiziellen Jupyter Base-Notebook Image.
# Dieses Image enthält die grundlegenden Jupyter-Komponenten, die wir benötigen.
FROM jupyter/base-notebook:latest

# Wechsel zum Root-Benutzer, um Systempakete zu installieren
USER root

# Führe das Update der Paketliste aus und installiere git, das wir für einige Operationen benötigen.
# "apt-get update" holt die neuesten Paketinformationen und "apt-get install" installiert git.
# Das "--no-install-recommends" stellt sicher, dass nur die grundlegendsten Pakete installiert werden,
# ohne unnötige zusätzliche Software.
# Am Ende löschen wir die Paketcache-Dateien, um den Container kleiner zu machen.
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && \
    rm -rf /var/lib/apt/lists/*

# Jetzt wechseln wir zurück zum normalen Benutzer (NB_USER),
# um sicherzustellen, dass alle weiteren Installationen im Kontext des Benutzers durchgeführt werden
# und nicht als Root, was eine bessere Sicherheitspraxis ist.
USER $NB_USER

# Kopiere die requirements.txt Datei von deinem lokalen Verzeichnis in das Container-Dateisystem
# Diese Datei enthält eine Liste von Python-Paketen, die später installiert werden.
COPY .devcontainer/requirements.txt /tmp/requirements.txt

# Erstelle ein Verzeichnis für die IPython-Startup-Skripte.
# IPython-Startups sind Skripte, die automatisch ausgeführt werden, wenn ein Jupyter Notebook oder IPython
# gestartet wird. Diese werden oft verwendet, um nützliche Importe oder Funktionen vorab zu definieren.
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

# Füge eine Zeile hinzu, die beim Starten von IPython Jupyter Lab Warnungen von pyflyby unterdrückt.
# Diese Zeile sorgt dafür, dass IPython beim Starten keine unnötigen Warnungen anzeigt, die dich darauf
# hinweisen, pyflyby zu installieren. Dies macht das Notebook-Environment sauberer und angenehmer zu nutzen.
RUN echo "import warnings\nwarnings.filterwarnings('ignore', category=UserWarning, module='pyflyby')" >> /home/$NB_USER/.ipython/profile_default/startup/00-startup.py

# Installiere alle Python-Pakete aus der requirements.txt-Datei, die wir im Container gespeichert haben.
# Die "pip install -r /tmp/requirements.txt"-Anweisung stellt sicher, dass alle Pakete, die für das Projekt
# notwendig sind, installiert werden. Dazu gehören u.a. Bibliotheken wie Pandas, NumPy, Matplotlib und andere.
RUN pip install -r /tmp/requirements.txt

# Installiere pyflyby und führe die Konfiguration für IPython aus.
# Hier installieren wir pyflyby explizit und führen dann den Befehl aus, um pyflyby in der IPython-Konfiguration
# zu registrieren. Dies stellt sicher, dass pyflyby korrekt konfiguriert ist, damit es in jedem Jupyter-Notebook
# verfügbar ist und funktioniert, ohne dass zusätzliche Schritte erforderlich sind.
RUN pip install pyflyby && \
    python -c "import pyflyby; pyflyby.install_in_ipython_config_file()"

# Der Standardbefehl für den Container, wenn er gestartet wird.
# Hier starten wir Jupyter Lab und geben an, dass es auf allen Netzwerkadressen verfügbar sein soll
# ("--ip=0.0.0.0") und auf Port 8888 läuft. 
# Wir deaktivieren den Browserstart und entfernen den Token, um eine einfache Verbindung ohne Authentifizierung zu ermöglichen.
# Das Verzeichnis, das geöffnet wird, wird auf /workspaces/SC_EA1_bis_EA3 gesetzt.
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.notebook_dir=/workspaces/SC_EA1_bis_EA3"]
