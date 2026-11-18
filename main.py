#!/usr/bin/env python3
"""Sum up the world's news of Wednesday 18 November 2026 in one image.

Entry program for the make.fun news-image-20261118 competition.
The entry image is committed in this repository as entry.png (a
newspaper front page composed from an original illustration and the
day's headlines). This program copies it, byte for byte, to
/output/entry.png, creating /output if needed, so every run produces
the same image.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"entry image not found: {src}")
    dst = Path("/output/entry.png")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    size = src.stat().st_size
    if dst.stat().st_size != size:
        raise IOError(f"copy size mismatch: wrote {dst.stat().st_size} of {size} bytes")
    print(f"Wrote {dst} ({size} bytes, size verified).")


if __name__ == "__main__":
    main()
