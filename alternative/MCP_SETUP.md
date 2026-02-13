# MCP Server Setup (Alternative Approach)

Wenn du die Bildanalyse als **MCP-Server** statt CLI-Tool nutzen möchtest, folge dieser Anleitung.

## 🔄 CLI vs MCP Vergleich

| Aspekt | CLI-Tool (Standard) | MCP-Server |
|--------|---------------------|------------|
| Context Usage | 0 tokens (Skill: 261 tokens) | 155 tokens (permanent) |
| Aufruf | `python3 main.py <bild>` | Direkter Tool-Aufruf |
| Lazy Loading | ✅ Ja | ❌ Nein |
| Setup | Einfach (Skill) | Erfordert MCP-Config |
| Empfohlen für | Seltene Nutzung | Häufige Nutzung |

## 📦 MCP-Server Setup

### Schritt 1: MCP-Server registrieren

Bearbeite `~/.claude/settings.json` und füge hinzu:

```json
{
  "model": "sonnet",
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

**Wichtig:** Ersetze `DEIN_USERNAME` mit deinem tatsächlichen Username!

### Schritt 2: Claude Code neu starten

```bash
# Beende Claude Code und starte neu
# Oder nutze:
/reload mcp
```

### Schritt 3: Testen

```bash
# In Claude Code:
# Das MCP-Tool ist jetzt verfügbar als:
mcp__ollama-vision__analyze_local_image
```

## 🎯 Verwendung

### Direkt im Chat

```
User: "Analysiere das Bild ~/Desktop/screenshot.png"
Claude: [nutzt automatisch mcp__ollama-vision__analyze_local_image]
```

### Mit Custom Prompt

Das MCP-Tool akzeptiert zwei Parameter:
- `image_path` (required): Vollständiger Pfad zum Bild (mit Dateiendung!)
- `prompt` (optional): Custom Prompt (Standard: "Beschreibe dieses Bild kurz.")

Beispiel:
```python
mcp__ollama-vision__analyze_local_image(
    image_path="/Users/gasser/Desktop/rechnung.png",
    prompt="Extrahiere alle Beträge und Rechnungsnummern"
)
```

## ⚠️ Wichtige Unterschiede zum CLI-Tool

### CLI-Tool (`main.py`)
- ✅ Automatische Dateiendungs-Erkennung
- ✅ Glob-Pattern-Support
- ✅ Robuste Fehlerbehandlung
- ✅ Schöne formatierte Ausgabe

### MCP-Server (`mcp_image_extract.py`)
- ❌ **Erfordert vollständige Dateiendung** (.png, .jpg, etc.)
- ✅ Direkter Tool-Aufruf (schneller)
- ✅ Typsichere API

## 🔧 MCP-Server anpassen

Bearbeite `mcp_image_extract.py` um:

### Anderes Modell verwenden
```python
# Zeile 16 ändern:
model='llama3.2-vision:11b'  # Statt qwen3-vl:4b
```

### Standard-Prompt ändern
```python
# Zeile 8 ändern:
def analyze_local_image(image_path: str, prompt: str = "DEIN PROMPT") -> str:
```

## 📊 Context-Vergleich

### Nur CLI (Empfohlen)
```
Skills: 261 tokens (ollama-vision, wenn geladen)
MCP: 0 tokens
TOTAL: 261 tokens (oder 0 wenn Skill nicht aktiv)
```

### Nur MCP
```
Skills: 0 tokens
MCP: 155 tokens (permanent)
TOTAL: 155 tokens (immer)
```

### CLI + MCP (Nicht empfohlen - Doppelung!)
```
Skills: 261 tokens
MCP: 155 tokens
TOTAL: 416 tokens (ineffizient!)
```

## 🎓 Wann MCP nutzen?

**✅ Nutze MCP wenn:**
- Du Bildanalyse mehrmals täglich brauchst
- Du einen sauberen API-Aufruf bevorzugst
- 155 tokens permanent OK sind

**✅ Nutze CLI wenn:**
- Du Bildanalyse selten nutzt (< 1x pro Tag)
- Du Context sparen möchtest (Lazy Loading)
- Du maximale Flexibilität brauchst

## 🔄 Von MCP zurück zu CLI

1. Entferne den MCP-Server aus `settings.json`
2. Reload: `/reload mcp`
3. Nutze den Skill wie gewohnt: `/ollama-vision <bild>`

---

**Empfehlung:** Bleib bei CLI-only für optimalen Context-Verbrauch! MCP nur bei wirklich häufiger Nutzung sinnvoll.
