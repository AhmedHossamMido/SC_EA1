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
   Klicken Sie oben auf **"Ports"** → **Port 8888** → **"Open in Browser"**.

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

Kontakt & Hinweise
------------------

- Änderungen im Codespace können direkt via Git gepusht werden.
- Die Umgebung wurde für eine einfache Nutzung in Browser und Codespaces optimiert.
- Bei Fragen oder Feedback gerne im GitHub-Issue melden.
