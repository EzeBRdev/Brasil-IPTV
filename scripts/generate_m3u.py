import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANNELS_FILE = ROOT / "sources/channels.json"
OUTPUT_FILE = ROOT / "dist/brasil-iptv.m3u"

def main():
    with CHANNELS_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    lines = ["#EXTM3U"]

    for channel in data.get("channels", []):
        name = channel.get("name")
        url = channel.get("url")

        if not name or not url:
            continue

        lines.append(f"#EXTINF:-1,{name}")
        lines.append(url)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )

    print(f"Playlist criada: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
