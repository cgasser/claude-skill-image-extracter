---
name: ollama-vision
description: Extrahiert Informationen aus Bildern mit einem lokalen Vision-Modell (Ollama). Nutze dies, wenn der User nach Inhalten eines lokalen Bildes fragt.
dependencies: python>=3.8, ollama
---

# Ollama Bild-Extraktion

Verwende diesen Skill, um lokale Bilddateien zu analysieren.

## Benutzung
Führe das Python-Skript aus, um ein Bild zu verarbeiten:
`python3 ~/repo/claude-skill-image-extracter/main.py <pfad_zum_bild> [optionaler_prompt]`

**Hinweis**: Die Dateiendung (.png, .jpg, etc.) wird automatisch erkannt!

## Beispiele
- "Was steht auf dem Bild unter ./images/rechnung.jpg?"
- "Extrahiere den Text aus screenshot.png."
- "Analysiere ~/Desktop/error" (Dateiendung wird automatisch gefunden)

## Features
- ✅ Automatische Bildformat-Erkennung
- ✅ Custom Prompts für spezifische Fragen
- ✅ Robuste Fehlerbehandlung
- ✅ 100% lokal & privat
