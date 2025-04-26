FROM jupyter/base-notebook:latest

# Installiere zusätzliche Pakete
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && \
    rm -rf /var/lib/apt/lists/*

# Wechsel zurück zum normalen User
USER $NB_USER

# Installiere Python-Abhängigkeiten
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# IPython Startup Imports automatisch erstellen
RUN mkdir -p /home/$NB_USER/.ipython/profile_default/startup && \
    echo "import marimo\nimport pyflyby\nimport altair as alt\nimport hvplot\nimport matplotlib.pyplot as plt\nimport numba\nimport numpy as np\nimport pandas as pd\nimport plotly.express as px\nimport polars as pl\nimport pyarrow\nimport scipy" > /home/$NB_USER/.ipython/profile_default/startup/00-startup.py

# Standard-Startbefehl
CMD ["start-notebook.sh"]
