"""Give the vegetable drawer one compact roast.
Lettuce retiring supplies a concrete image and a single closing twist.
"""

import hashlib
import os
from pathlib import Path
import tempfile


LINE = "Vegetable drawer: where lettuce goes to retire."


def _resolve_output_dir() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        output_dir = Path(tempfile.mkdtemp(prefix="makefun-fridge-"))
    return output_dir


def validate(path: Path) -> None:
    content = path.read_bytes()
    text = content.decode("utf-8")
    if content != LINE.encode("utf-8"):
        raise ValueError("Entry bytes differ from LINE")
    if text != LINE:
        raise ValueError("Entry text differs from LINE")
    if not 1 <= len(text) <= 199:
        raise ValueError("Entry must contain 1-199 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("Entry must be one line")
    if content.endswith((b"\n", b"\r")):
        raise ValueError("Trailing newline is forbidden")
    if text != text.strip():
        raise ValueError("Surrounding whitespace is forbidden")


def main() -> None:
    path = _resolve_output_dir() / "entry.txt"
    path.write_bytes(LINE.encode("utf-8"))
    validate(path)
    print(hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
