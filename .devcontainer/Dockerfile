FROM jupyter/base-notebook:latest

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# IPython Startup Imports (direkt im Build)
RUN mkdir -p /home/$NB_USER/.ipython/profile_default/startup && \
    echo "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport altair as alt\nimport plotly.express as px\nimport polars as pl\nimport pyarrow\nimport scipy\nimport marimo\nimport hvplot\nimport numba" > /home/$NB_USER/.ipython/profile_default/startup/00-startup.py

CMD ["start-notebook.sh"]
