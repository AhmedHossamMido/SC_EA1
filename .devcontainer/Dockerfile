FROM jupyter/base-notebook:latest

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && \ 
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["start-notebook.sh"]

# IPython Startup Imports
COPY .devcontainer/ipython_startup_imports.py /home/$NB_USER/.ipython/profile_default/startup/00-imports.py
