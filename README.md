# Projektname

Dieses Projekt ist für die Verwendung mit [GitHub Codespaces](https://github.com/features/codespaces) konzipiert, einer Cloud-basierten Entwicklungsumgebung. Der Container wird mit einem **Dockerfile** erstellt und eine Reihe von Python-Paketen werden automatisch installiert, um eine schnelle Entwicklungsumgebung für das Projekt bereitzustellen.

## Inhalt des Repositories

Das Repository enthält drei Hauptdateien, die für die Konfiguration des Devcontainers in GitHub Codespaces verwendet werden:

1. **Dockerfile**:  
   Dieses Dockerfile definiert, wie der Entwicklungscontainer gebaut wird. Es basiert auf einem Jupyter-Image und installiert alle notwendigen System- und Python-Abhängigkeiten, die für das Projekt benötigt werden.
   
   - Es enthält die Installation von Python sowie einer Reihe von Python-Paketen, die für die Arbeit mit Jupyter Notebooks und wissenschaftlichen Anwendungen erforderlich sind, wie `pandas`, `matplotlib`, `numpy`, `scipy` und viele andere.
   - Zudem wird die Installation von `marimo` und verwandten Tools für die Visualisierung und Profilerstellung vorbereitet.
   
2. **devcontainer.json**:  
   Diese Datei konfiguriert den GitHub Codespace und den Devcontainer, der beim Starten des Codespaces verwendet wird. Sie enthält folgende Konfigurationen:
   - Das Dockerfile, das verwendet wird, um den Container zu erstellen.
   - Wichtige Erweiterungen, die in der Codespace-Umgebung installiert werden, wie z. B. Python, Jupyter, und GitHub Copilot.
   - Befehle, die nach der Erstellung des Containers ausgeführt werden, um Python-Pakete aus der `requirements.txt` zu installieren und den Jupyter-Server für die Nutzung vorzubereiten.

3. **requirements.txt**:  
   Diese Datei listet alle Python-Abhängigkeiten auf, die im Container installiert werden müssen. Sie enthält wichtige wissenschaftliche Bibliotheken wie `numpy`, `pandas`, `matplotlib`, `scipy` und viele mehr, die für die Datenanalyse und Visualisierung verwendet werden.

## So funktioniert der Container:

1. **Dockerfile**:  
   Der Container wird basierend auf einem Jupyter-Base-Notebook-Image gebaut. Das Dockerfile stellt sicher, dass alle notwendigen Abhängigkeiten und Tools für das Projekt installiert werden, einschließlich Python, JupyterLab und die in `requirements.txt` angegebenen Pakete.

2. **devcontainer.json**:  
   Diese Datei sorgt dafür, dass GitHub Codespaces beim Öffnen des Repositories den richtigen Container baut und ausführt. Sie definiert außerdem, welche Erweiterungen (wie Python und Jupyter) installiert werden sollen und führt Skripte aus, um sicherzustellen, dass alle Python-Pakete aus `requirements.txt` korrekt installiert sind.

3. **requirements.txt**:  
   Diese Datei sorgt dafür, dass beim Starten des Codespaces alle benötigten Python-Bibliotheken automatisch installiert werden. Sie enthält alle wissenschaftlichen Pakete, die für das Arbeiten mit Daten und die Visualisierung erforderlich sind.

## Schritte zum Starten:

1. **GitHub Codespace erstellen**:  
   - Gehe zu deinem Repository auf GitHub.
   - Klicke auf den **"Code"** Button und wähle **"Open with Codespaces"**.
   - Klicke auf **"New codespace"**.
   
2. **Automatische Installation**:  
   Beim Öffnen des Codespaces wird der Container basierend auf dem `Dockerfile` gebaut und alle Abhängigkeiten aus `requirements.txt` installiert.

3. **Arbeiten im Codespace**:  
   Nach dem Start des Codespaces hast du eine voll funktionsfähige Entwicklungsumgebung, die bereit ist, um mit Python und Jupyter Notebooks zu arbeiten.

## Zusätzliche Informationen

- GitHub Codespaces bietet eine leistungsstarke cloudbasierte Entwicklungsumgebung, die das Setup und die Verwaltung von Entwicklungsumgebungen vereinfacht.
- Der Container kann auch lokal über Docker oder andere Plattformen verwendet werden, indem du das Dockerfile und die anderen Konfigurationsdateien verwendest.

---

Viel Spaß beim Arbeiten mit GitHub Codespaces! Wenn du Fragen hast, kannst du dich gerne melden.
