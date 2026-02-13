# Ollama Vision Image Analyzer

Lokale Bildanalyse mit Ollama Vision Models für Claude Code. Analysiere Bilder, Screenshots und Dokumente ohne externe APIs - alles lokal auf deinem Rechner.

## ✨ Features

- 🖼️ **Automatische Format-Erkennung** - Keine Dateiendung nötig (.png, .jpg, .jpeg, .gif, .webp, .bmp, .tiff)
- 🎯 **Custom Prompts** - Stelle spezifische Fragen an das Bild
- 🔒 **100% Lokal & Privat** - Bilder verlassen nie deinen Computer
- ⚡ **Schnell** - Nutzt lokales Ollama qwen3-vl:4b Modell
- 💡 **Null Context-Overhead** - Nur geladen wenn benötigt (CLI-Ansatz)

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
   pip install ollama
   ```

## 🚀 Verwendung

### 1. Als CLI-Tool (Empfohlen)

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

### 3. Als MCP-Server (Optional)

Für häufige Nutzung kannst du auch den MCP-Server nutzen.
**📖 Siehe [alternative/MCP_SETUP.md](alternative/MCP_SETUP.md) für Details.**

**Vergleich:**
- **CLI** (Standard): 0 tokens wenn nicht genutzt, Lazy Loading ✅
- **MCP** (Optional): 155 tokens permanent, direkter Tool-Aufruf ⚡

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

### Ohne Dateiendung
```bash
python3 main.py ~/Desktop/Bildschirmfoto  # Findet automatisch .png
```

## 🏗️ Projekt-Struktur

```
claude-skill-image-extracter/
├── main.py                  # ⭐ CLI-Tool (empfohlen)
├── SKILL.md                 # Skill-Beschreibung für Claude Code
├── README.md                # Diese Datei
├── requirements.txt         # Python-Abhängigkeiten
├── LICENSE                  # MIT Lizenz
├── alternative/             # Alternative Ansätze & Dokumentation
│   ├── MCP_SETUP.md        # 📖 MCP-Server Setup-Anleitung
│   ├── mcp_image_extract.py # MCP-Server-Implementierung
│   ├── CLAUDE.md            # OCR-Projekt-Planung (erweitert)
│   └── OCR_SOLUTION_ANALYSIS.md
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

Um ein anderes Modell zu verwenden, editiere `main.py` und ändere den `model`-Parameter in Zeile 51:

```python
response = ollama.chat(
    model='llama3.2-vision:11b',  # Ändere hier
    messages=[...]
)
```

## 🎨 CLI vs MCP - Wann was nutzen?

### ✅ Nutze CLI (Standard) wenn:
- Du Bildanalyse **selten** brauchst (< 1x pro Tag)
- Du **Context sparen** möchtest (0 tokens wenn nicht genutzt)
- Du **maximale Flexibilität** brauchst (auto file detection)

### ⚡ Nutze MCP (Optional) wenn:
- Du Bildanalyse **häufig** brauchst (mehrmals täglich)
- Du **direkten Tool-Aufruf** bevorzugst
- 155 tokens permanent OK sind

**📖 [MCP Setup-Anleitung →](alternative/MCP_SETUP.md)**

## 📝 Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## 🤝 Beitragen

Contributions sind willkommen! Bitte öffne ein Issue oder Pull Request.

## 🐛 Fehler melden

Bei Problemen bitte ein Issue auf [GitHub](https://github.com/cgasser/claude-skill-image-extracter/issues) erstellen mit:
- Beschreibung des Problems
- Python-Version (`python3 --version`)
- Ollama-Version (`ollama --version`)
- Verwendetes Modell
- Fehlermeldung (falls vorhanden)

## 💡 Tipps

- **Größere Modelle**: Für bessere Genauigkeit nutze `llama3.2-vision:11b` (benötigt mehr RAM)
- **Schnellere Analyse**: Nutze `moondream` für Edge-Devices
- **Mehrsprachig**: Passe den Prompt an, z.B. "Describe in German..."
- **Batch-Processing**: Nutze ein Shell-Script, um mehrere Bilder zu verarbeiten

## 🔗 Links

- **Repository**: https://github.com/cgasser/claude-skill-image-extracter
- **Ollama**: https://ollama.com
- **Claude Code**: https://claude.com/claude-code
- **Model (qwen3-vl)**: https://ollama.com/library/qwen3-vl
