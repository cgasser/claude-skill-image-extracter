import ollama
import os
import sys
import glob

def find_image_file(path):
    """
    Findet die Bilddatei, auch wenn die Endung fehlt.
    Versucht automatisch gängige Bildformate (.png, .jpg, .jpeg, .gif, .webp)
    """
    # Wenn die Datei bereits existiert, direkt zurückgeben
    if os.path.isfile(path):
        return path

    # Versuche gängige Bildformate
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.tiff']

    for ext in image_extensions:
        test_path = path + ext
        if os.path.isfile(test_path):
            print(f"✓ Datei gefunden: {test_path}")
            return test_path

    # Versuche Glob-Pattern (falls Wildcards verwendet werden)
    matches = glob.glob(path + '*')
    image_matches = [m for m in matches if os.path.isfile(m) and
                     any(m.lower().endswith(ext) for ext in image_extensions)]

    if image_matches:
        print(f"✓ Datei gefunden: {image_matches[0]}")
        return image_matches[0]

    return None

def analyze_image(image_path, prompt=None):
    """
    Analysiert ein Bild mit Ollama Vision Model

    Args:
        image_path: Pfad zum Bild
        prompt: Optionaler benutzerdefinierter Prompt
    """
    # Standardprompt falls keiner angegeben
    if prompt is None:
        prompt = 'Was ist auf diesem Bild zu sehen? Beschreibe es detailliert.'

    print(f"Starte Analyse für: {image_path}")

    try:
        response = ollama.chat(
            model='qwen3-vl:4b',
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }]
        )

        print("\n" + "="*60)
        print("Ollama Analyse:")
        print("="*60)
        print(response['message']['content'])
        print("="*60)

    except Exception as e:
        print(f"\n❌ Fehler bei der Ollama-Analyse: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("❌ Fehler: Kein Bildpfad angegeben!")
        print("\nVerwendung:")
        print("  python3 main.py <pfad_zum_bild> [optionaler_prompt]")
        print("\nBeispiele:")
        print("  python3 main.py foto.png")
        print("  python3 main.py ~/Desktop/screenshot 'Extrahiere allen Text'")
        sys.exit(1)

    input_path = sys.argv[1]
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else None

    # Versuche die Datei zu finden
    image_path = find_image_file(input_path)

    if image_path is None:
        print(f"❌ Fehler: Bilddatei nicht gefunden: {input_path}", file=sys.stderr)
        print("\nHinweis: Gängige Bildformate werden automatisch erkannt (.png, .jpg, .jpeg, etc.)")
        sys.exit(1)

    # Überprüfe, ob es wirklich eine Datei ist (kein Verzeichnis)
    if not os.path.isfile(image_path):
        print(f"❌ Fehler: Pfad ist keine Datei: {image_path}", file=sys.stderr)
        sys.exit(1)

    # Analysiere das Bild
    analyze_image(image_path, custom_prompt)

if __name__ == "__main__":
    main()
