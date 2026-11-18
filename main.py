#!/usr/bin/env python3
"""Sum up the world's news of Wednesday 18 November 2026 in one image.

The entry image is committed in this repository as entry.png (a
newspaper front page composed from an original illustration and the
day's headlines). This program writes it to /output/entry.png, byte
for byte, so every run produces the same image.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
