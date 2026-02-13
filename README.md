# Ollama Vision Image Analyzer

Lokale Bildanalyse mit Ollama Vision Models für Claude Code. Analysiere Bilder, Screenshots und Dokumente ohne externe APIs - alles lokal auf deinem Rechner.

## ✨ Features

- 🖼️ **Automatische Format-Erkennung** - Keine Dateiendung nötig (.png, .jpg, .jpeg, .gif, .webp, .bmp, .tiff)
- 🎯 **Custom Prompts** - Stelle spezifische Fragen an das Bild
- 🔒 **100% Lokal & Privat** - Bilder verlassen nie deinen Computer
- ⚡ **Schnell** - Nutzt lokales Ollama qwen3-vl:4b Modell
- 🛠️ **Zwei Modi** - CLI-Tool oder MCP-Server

## 📦 Installation

### Voraussetzungen

1. **Ollama installieren**:
   ```bash
   # macOS/Linux
   curl -fsSL https://ollama.com/install.sh | sh

   # oder von https://ollama.com/download
   ```

2. **Vision Model herunterladen**:
   ```bash
   ollama pull qwen3-vl:4b
   ```

3. **Python-Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Verwendung

### 1. Als CLI-Tool

```bash
# Einfache Analyse
python3 main.py bild.jpg

# Ohne Dateiendung (wird automatisch erkannt)
python3 main.py ~/Desktop/screenshot

# Mit eigenem Prompt
python3 main.py rechnung.png "Extrahiere alle Beträge und Rechnungsnummern"
```

### 2. Als Claude Code Skill

Installiere den Skill in Claude Code:

```bash
# Verlinke oder kopiere das Skill
ln -s ~/repo/claude-skill-image-extracter ~/.claude/skills/ollama-vision
```

Dann in Claude Code:

```
/ollama-vision ~/Desktop/Bildschirmfoto
```

### 3. Als MCP-Server

Füge in `~/.claude/mcp_settings.json` hinzu:

```json
{
  "mcpServers": {
    "ollama-vision": {
      "command": "python3",
      "args": [
        "/Users/DEIN_USERNAME/repo/claude-skill-image-extracter/mcp_image_extract.py"
      ]
    }
  }
}
```

## 📖 Beispiele

### Textextraktion
```bash
python3 main.py dokument.png "Extrahiere allen Text"
```

### Formular-Analyse
```bash
python3 main.py formular.jpg "Liste alle Felder und ihre Werte auf"
```

### Screenshot-Beschreibung
```bash
python3 main.py screenshot.png
# Verwendet Standard-Prompt: "Was ist auf diesem Bild zu sehen? Beschreibe es detailliert."
```

## 🏗️ Projekt-Struktur

```
claude-skill-image-extracter/
├── main.py                  # CLI-Tool (empfohlen)
├── mcp_image_extract.py     # MCP-Server-Variante
├── SKILL.md                 # Skill-Beschreibung für Claude Code
├── CLAUDE.md                # Diese Projektdokumentation
├── README.md                # Nutzer-Dokumentation
├── requirements.txt         # Python-Abhängigkeiten
├── alternative/             # Referenzen für erweiterte OCR-Lösungen
└── test_data/              # Beispiel-Testbilder (optional)
```

## 🎯 Verwendete Technologien

- **[Ollama](https://ollama.com/)** - Lokale LLM-Runtime
- **qwen3-vl:4b** - Vision Language Model für Bildanalyse
- **Python 3.8+** - Programmiersprache
- **FastMCP** - Model Context Protocol Server (optional)

## 🔧 Konfiguration

Das Skript verwendet standardmäßig:
- **Modell**: `qwen3-vl:4b`
- **Ollama Host**: `http://localhost:11434`

Um ein anderes Modell zu verwenden, editiere `main.py` oder `mcp_image_extract.py` und ändere den `model`-Parameter.

## 📝 Lizenz

MIT License - siehe LICENSE Datei für Details.

## 🤝 Beitragen

Contributions sind willkommen! Bitte öffne ein Issue oder Pull Request.

## 🐛 Fehler melden

Bei Problemen bitte ein Issue auf GitHub erstellen mit:
- Beschreibung des Problems
- Python-Version (`python3 --version`)
- Ollama-Version (`ollama --version`)
- Verwendetes Modell
- Fehlermeldung (falls vorhanden)

## 💡 Tipps

- **Größere Modelle**: Für bessere Genauigkeit nutze `llama3.2-vision:11b` (benötigt mehr RAM)
- **Schnellere Analyse**: Nutze `moondream` für Edge-Devices
- **Mehrsprachig**: Passe den Prompt an, z.B. "Describe in German..."
