import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANNELS_FILE = ROOT / "sources/channels.json"
OUTPUT_FILE = ROOT / "dist/channels.json"

def main():
    with CHANNELS_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    channels = data.get("channels", [])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        json.dumps(
            channels,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )

    print(f"{len(channels)} canais preparados.")

if __name__ == "__main__":
    main()
