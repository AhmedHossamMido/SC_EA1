# Base image: Jupyter Notebook base image
FROM jupyter/base-notebook:latest

# Switch to root user to install dependencies
USER root

# Install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && \ 
    rm -rf /var/lib/apt/lists/*

# Switch back to the default notebook user
USER $NB_USER

# Copy the requirements.txt file and install the Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# IPython Startup Imports
COPY .devcontainer/ipython_startup_imports.py /home/$NB_USER/.ipython/profile_default/startup/00-imports.py

# Default command to start the Jupyter Notebook
CMD ["start-notebook.sh"]
