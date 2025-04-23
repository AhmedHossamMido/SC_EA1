FROM jupyter/base-notebook:latest

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    debuginfod build-essential && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["start-notebook.sh"]
