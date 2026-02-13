from fastmcp import FastMCP
import ollama

# Erstelle den Server
mcp = FastMCP("OllamaVision")

@mcp.tool()
def analyze_local_image(image_path: str, prompt: str = "Beschreibe dieses Bild kurz.") -> str:
    """
    Analysiert ein lokales Bild mit dem Modell qwen3-vl:4b.
    Args:
        image_path: Der absolute Pfad zur Bilddatei.
        prompt: Die Frage oder Anweisung zum Bild.
    """
    try:
        response = ollama.chat(
            model='qwen3-vl:4b',
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }]
        )
        return response['message']['content']
    except Exception as e:
        return f"Fehler bei der Bildanalyse: {str(e)}"

if __name__ == "__main__":
    mcp.run()
