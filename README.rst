SciPro Projekt - Jupyter Entwicklungsumgebung (Docker & Codespaces)
====================================================================

Dieses Repository enthält eine vollständige JupyterLab-Umgebung für das SciPro-Projekt,
bereitgestellt als GitHub Codespace und Docker-Container.

Nutzung mit GitHub Codespaces (empfohlen)
------------------------------------------

1. **Repository öffnen**:
   Besuchen Sie das Repository auf GitHub.

2. **Codespace starten**:
   Klicken Sie auf den grünen Button **"Code"** → **"Open with Codespaces"** → **"New codespace"**.

3. **JupyterLab manuell öffnen**:
   Nach dem Start erscheint ein Hinweis, dass der Port 8888 offen ist.
   Klicken Sie auf **"Ports"** → **Port 8888** → **"Open in Browser"**.

4. **Arbeiten im Browser**:
   Die vollständige Jupyter-Umgebung ist im Browser verfügbar.
   Sie können Notebooks bearbeiten, speichern und über Git versionieren.

Inhalt des Containers
---------------------

- Basierend auf: ``jupyter/base-notebook:latest``
- Installierte Bibliotheken:
  - pandas, numpy, matplotlib, plotly, polars, altair, scipy, pyarrow u.v.m.
- Tools:
  - JupyterLab + Erweiterungen
  - Python 3 (Conda Umgebung)
- Entwicklungsumgebung: GitHub Codespaces

Features
--------

- **JupyterLab** in einem containerisierten Codespace
- Unterstützt moderne Datenanalyse-Tools wie `pandas`, `polars`, `plotly`, `altair`, `hvplot`, u. v. m.
- Performance-Analyse mit `memray`, `scalene`, `viztracer`, `numba`
- Erweiterbar durch VS Code Extensions (`Jupyter`, `Python`)
- Reproduzierbare Umgebung via `Dockerfile` & `requirements.txt`

Alternative: Lokale Ausführung (optional)
-----------------------------------------

1. Docker installieren (falls nicht vorhanden)
2. Projekt klonen:

   .. code-block:: bash

      git clone https://github.com/AhmedHossamMido/SC_EA1_bis_EA3.git
      cd SC_EA1_bis_EA3

3. Container bauen und starten:

   .. code-block:: bash

      docker build -t scipro-container .
      docker run -p 8888:8888 scipro-container

4. JupyterLab im Browser öffnen:
   Besuche http://localhost:8888 (Token wird in der Konsole angezeigt, wenn nötig).

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

- Die Arbeit mit Jupyter über den Codespace ist im Hinblick auf die Dateigröße eingeschränkt. 
- HTTP PUT/POST-Anfrage mit dem Notebook-Inhalt darf die HTTP-Größenbeschränkungen nicht überschreiten.
- Die Anfrage wird durch GitHub Codespaces oder den Jupyter-Server mit "413 Payload Too Large" abgelehnt, wenn die Datei zu groß ist
- Für größere Dateien empfiehlt es sich, lokal zu arbeiten.

Lizenz
------

MIT – frei verwendbar mit Attribution

