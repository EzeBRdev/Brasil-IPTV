import json
from pathlib import Path

FILES = [
    "sources/channels.json",
    "sources/playlists.json",
    "sources/epg_sources.json",
    "sources/logos.json",
]

def main():
    for filename in FILES:
        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {filename}")

        with path.open("r", encoding="utf-8") as file:
            json.load(file)

        print(f"[OK] {filename}")

    print("\nTodos os arquivos JSON são válidos!")

if __name__ == "__main__":
    main()
