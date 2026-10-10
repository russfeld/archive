#!/usr/bin/env python3
"""One-time fixes for internal links that were already broken in the original site.

Kept in the repo for provenance. Run once from the repo root:  python3 tools/fix-links.py
Missing images are copied from an identical-named copy elsewhere in the archive;
duplicate files are later collapsed to symlinks by tools/dedup.py.
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def edit(rel, old, new, count=1):
    p = ROOT / rel
    text = p.read_text(encoding="utf-8", errors="surrogateescape")
    if text.count(old) != count:
        sys.exit(f"{rel}: expected {count} of {old!r}, found {text.count(old)}")
    p.write_text(text.replace(old, new), encoding="utf-8", errors="surrogateescape")


def copy_if_missing(dst, src):
    d, s = ROOT / dst, ROOT / src
    if not d.exists():
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(s, d)


# 1. Big data / informatics decks copied from Spring 2015 into a subfolder of later
#    semesters kept <BASE href="../">, so every root-relative path missed by one level.
COPIED_DECKS = [
    "cis115fall2015/21informatics", "cis115spring2016/26informatics",
    "cis115fall2016/27informatics", "cis115spring2017/27informatics",
]
for d in COPIED_DECKS:
    for deck in ("lecture18.html", "lecture28.html"):
        rel = f"{d}/{deck}"
        edit(rel, '<BASE href="../">', '<BASE href="../../">')
        # Images added after Spring 2015 only exist in the semester's own images/ folder.
        p = ROOT / rel
        text = p.read_text(encoding="utf-8", errors="surrogateescape")
        def local(m):
            if (ROOT / m.group(1)).exists():
                return m.group(0)
            name = Path(m.group(1)).name
            if not (ROOT / d / "images" / name).exists():
                sys.exit(f"{rel}: no copy of {name}")
            return f'src="{d}/images/{name}"'
        p.write_text(re.sub(r'src="(cis115spring2015/images/lecture\d+/[^"]+)"', local, text),
                     encoding="utf-8", errors="surrogateescape")

# 2. "wireframe" image referenced without its .png extension.
WIREFRAME = "cis115fall2014/images/lecture23/wireframe.png"
for rel, src in [
    ("cis115spring2017/17graphics/index.html", "images/wireframe"),
    ("cis115fall2016/20graphics/index.html", "images/wireframe"),
    ("cis115spring2016/20graphics/index.html", "images/wireframe"),
    ("cis115fall2015/23graphics/index.html", "images/wireframe"),
    ("cis115spring2014/lecture23.html", "cis115spring2014/images/lecture23/wireframe"),
    ("cis115spring2015/lecture19.html", "cis115spring2015/images/lecture19/wireframe"),
    ("cis115fall2013/lecture10.html", "cis115fall2013/images/lecture10/wireframe"),
]:
    edit(rel, f'src="{src}"', f'src="{src}.png"')
    # Course-prefixed paths are resolved from the site root (via <BASE>); others from the page's folder.
    dst = f"{src}.png" if src.startswith("cis") else f"{Path(rel).parent}/{src}.png"
    copy_if_missing(dst, WIREFRAME)

# 3. Spring 2015 syllabus images were never copied into that semester.
for name in ("grades.png", "dontpanic_vantaj.jpg"):
    copy_if_missing(f"cis115spring2015/images/syllabus/{name}", f"cis115fall2014/images/syllabus/{name}")

# 4. CIS 527 Spring 2015 lecture 21 pointed at the site-wide images/ folder.
for name in ("harddrive_walkn_flickr.jpg", "rto_rpo_wiki.jpg", "higha_wiki.png"):
    edit("cis527spring2015/lecture21.html", f'src="images/{name}"',
         f'src="cis527spring2015/images/lecture21/{name}"')
    copy_if_missing(f"cis527spring2015/images/lecture21/{name}", f"cis527spring2016/27backups/images/{name}")

# 5. Typo (stray space) in the 2014 rules book link.
edit("openhouse/index.html", 'href="openhouse /files/2014/0rules.pdf"', 'href="openhouse/files/2014/0rules.pdf"')

# 6. Lectures that were linked but never posted.
edit("cis527spring2015/index.html", '<a href="cis527spring2015/lecture20.html">Lecture 20 - Web Servers</a>',
     "Lecture 20 - Web Servers (not available)")
edit("cis527spring2016/index.html", '<a href="cis527spring2016/14winad">Lecture 14 - Windows Active Directory</a>',
     "Lecture 14 - Windows Active Directory (not available)")
edit("cis527spring2016/index.html", '<a href="cis527spring2016/15ldap">Lecture 15 - LDAP</a>',
     "Lecture 15 - LDAP (not available)")

# 7. Scholars page (no <BASE>) pointed at a favicon in its own folder.
edit("cis115fall2016/scholars/index.html", '<link href="favicon.ico" rel="shortcut icon">',
     '<link href="/favicon.ico" rel="shortcut icon">')

print("done")
