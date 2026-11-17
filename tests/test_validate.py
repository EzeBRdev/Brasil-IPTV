import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class TestBrasilIPTV(unittest.TestCase):

    def test_arquivos_json_validos(self):
        arquivos = [
            "sources/channels.json",
            "sources/playlists.json",
            "sources/epg_sources.json",
            "sources/logos.json",
        ]

        for arquivo in arquivos:
            caminho = ROOT / arquivo

            self.assertTrue(
                caminho.exists(),
                f"Arquivo não encontrado: {arquivo}"
            )

            with caminho.open("r", encoding="utf-8") as file:
                dados = json.load(file)

            self.assertIsInstance(dados, dict)

    def test_estrutura_dos_canais(self):
        caminho = ROOT / "sources/channels.json"

        with caminho.open("r", encoding="utf-8") as file:
            dados = json.load(file)

        self.assertIn("channels", dados)
        self.assertIsInstance(dados["channels"], list)

if __name__ == "__main__":
    unittest.main()
