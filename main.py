"""Deliver the 18 November 2026 front page for judging.

This repository holds the finished artwork as entry.png beside this
file. Executing the file places a faithful copy at /output/entry.png
and then compares the copy against the original byte by byte before
reporting success, so Wednesday 18 November 2026 is summed up in one
image exactly as it was composed.
"""

import pathlib

ARTWORK_NAME = "entry.png"
OUTPUT_FILE = pathlib.Path("/output") / "entry.png"


def read_artwork():
    here = pathlib.Path(__file__).resolve().parent
    artwork = here / ARTWORK_NAME
    if not artwork.is_file():
        raise SystemExit("artwork missing beside the script: " + str(artwork))
    return artwork.read_bytes()


def place_copy(data):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(data)
    return OUTPUT_FILE


def entry_point():
    data = read_artwork()
    if not data:
        raise SystemExit("artwork file is empty, refusing to deliver")
    placed = place_copy(data)
    if placed.stat().st_size != len(data):
        raise SystemExit("the delivered copy has the wrong size")
    if placed.read_bytes() != data:
        raise SystemExit("the delivered copy does not match the artwork")
    print("front page delivered to %s (%d bytes, match confirmed)" % (placed, len(data)))


entry_point()
