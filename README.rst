SciPro Containerumgebung
=========================

Dies ist ein Docker- und GitHub-Codespace-basiertes JupyterLab-Projekt für datenintensive Python-Projekte (z. B. für wissenschaftliches Programmieren, Visualisierungen und Performance-Analysen).

Features
--------

- **JupyterLab** in einem containerisierten Codespace
- Unterstützt moderne Datenanalyse-Tools wie `pandas`, `polars`, `plotly`, `altair`, `hvplot`, u. v. m.
- Performance-Analyse mit `memray`, `scalene`, `viztracer`, `numba`
- Erweiterbar durch VS Code Extensions (`Jupyter`, `Python`)
- Reproduzierbare Umgebung via `Dockerfile` & `requirements.txt`

Schnellstart
------------

1. **Codespace starten**

   Öffne dieses Repository in einem GitHub Codespace. Die Umgebung wird automatisch gebaut und JupyterLab startet auf Port ``8888``.

2. **JupyterLab verwenden**

   Die Lab-Oberfläche öffnet sich automatisch. Alternativ:

   .. code-block:: bash

      jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

3. **Notebooks bearbeiten**

   Öffne oder erstelle Jupyter Notebooks im ``/workspaces/``-Verzeichnis.

4. **Änderungen committen**

   Git ist im Container vorinstalliert. Du kannst deine Änderungen wie gewohnt versionieren:

   .. code-block:: bash

      git add .
      git commit -m "Meine Änderungen"
      git push

Struktur
--------

- ``Dockerfile`` – definiert die Containerumgebung (inkl. Git & Python libs)
- ``requirements.txt`` – alle Python-Abhängigkeiten
- ``.devcontainer/`` – Konfiguration für GitHub Codespaces
- ``.vscode/`` – optional: Python- und Jupyter-Einstellungen

Hinweise
--------

- Beim ersten Push wirst du ggf. nach deinem GitHub Token oder SSH-Zugang gefragt.
- Erweiterungen wie `jupyterlab_pyflyby` und `marimo` sind bereits vorinstalliert.
- Beachte, dass Notebook 7 Änderungen an alten Erweiterungen verursachen kann: https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html

Lizenz
------

MIT – frei verwendbar mit Attribution
