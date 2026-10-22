import json
from pathlib import Path
from random import choice

_PACKAGE_DIR = Path(__file__).parent
_VOCAB_PATH = _PACKAGE_DIR / "data" / "vocab.json"

with open(_VOCAB_PATH, "rb") as f:
    dictionary = json.load(f)

def letov(model: str = "mlp", min_length: int = 5, max_length: int = 15) -> str:
    song = choice(dictionary)
    line = choice(song["lyrics"])
    return line


def main() -> None:
    print(letov())