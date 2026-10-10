#!/usr/bin/env python3
"""Replace duplicate (byte-identical) non-HTML files with relative symlinks to one copy.

Course decks were copied semester to semester with their images, so most of the
archive's size is duplicates. Git already stores identical blobs once; this shrinks
the checkout and the Docker image. HTML pages are never linked, so editing one page
can't silently change another. nginx follows the symlinks (they stay inside the root).

Safe to re-run: existing symlinks are skipped. Usage:  python3 tools/dedup.py
"""
import hashlib
import os
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_TOP = {".git", ".github", "tools", "nginx"}
SKIP_SUFFIX = {".html", ".htm"}


def files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = Path(dirpath).relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP_TOP:
            dirnames[:] = []
            continue
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_symlink() or p.suffix.lower() in SKIP_SUFFIX or rel == Path("."):
                continue
            yield p


def main():
    groups = defaultdict(list)
    for p in files():
        groups[hashlib.sha256(p.read_bytes()).hexdigest()].append(p)

    linked = saved = 0
    for paths in groups.values():
        if len(paths) < 2:
            continue
        # Keep the copy with the shortest, then alphabetically first, path.
        paths.sort(key=lambda p: (len(p.parts), str(p)))
        keep = paths[0]
        for dup in paths[1:]:
            saved += dup.stat().st_size
            dup.unlink()
            dup.symlink_to(os.path.relpath(keep, dup.parent))
            linked += 1
    print(f"linked {linked} duplicates, saved {saved / 1e6:.0f} MB")


if __name__ == "__main__":
    main()
