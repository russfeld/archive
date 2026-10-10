#!/usr/bin/env python3
"""One-time conversion of the old cs.ksu.edu/~russfeld PHP site to static HTML.

The site only ever used PHP for `<?php include("...") ?>` of a shared header/footer
and one `$projectRoot` echo in header.php, so this reproduces that exactly:

  * every *.php page (except the include-only header.php) is rendered to *.html
    next to it, with includes inlined;
  * links to *.php pages are rewritten to *.html;
  * absolute /~russfeld/ paths and http://people.cis.ksu.edu/~russfeld/ links
    become root-relative (site now served at /);
  * the *.php sources are removed.

Kept in the repo for provenance. Run once from the repo root:  python3 tools/render-php.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INCLUDE_ONLY = {"header.php", "footer.html", "footernav.html"}

INCLUDE_RE = re.compile(r'<\?php\s+include\("([^"]+)"\);\s*\?>')
SETUP_RE = re.compile(r'\A<\?php.*?\?>\s*', re.S)  # header.php's $projectRoot setup block
PROJECT_ROOT_RE = re.compile(r'<\?php\s+echo\s+\$projectRoot;\s*\?>')
PHP_LINK_RE = re.compile(r'((?:href|action)=")([^"#?:]*?)\.php([#?"])', re.I)
TILDE_RE = re.compile(r'(["\'(])/~russfeld/')
OLD_HOST_RE = re.compile(r'((?:href|src)=")https?://people\.cis?\.ksu\.edu/~russfeld/?', re.I)


def render(path: Path, depth=0) -> str:
    text = path.read_text(encoding="utf-8", errors="surrogateescape")
    if path.name == "header.php":
        text = SETUP_RE.sub("", text)
        # Pages set <base> to the site root, so "./" means the root here.
        text = PROJECT_ROOT_RE.sub("./", text)
    if depth > 5:
        sys.exit(f"include depth exceeded at {path}")
    return INCLUDE_RE.sub(lambda m: render((path.parent / m.group(1)).resolve(), depth + 1), text)


def fix_links(text: str) -> str:
    text = PHP_LINK_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}.html{m.group(3)}", text)
    text = OLD_HOST_RE.sub(r"\1/", text)
    return TILDE_RE.sub(r"\1/", text)


def main():
    pages = sorted(p for p in ROOT.rglob("*.php") if p.relative_to(ROOT).as_posix() not in INCLUDE_ONLY)
    for page in pages:
        out = render(page)
        if "<?php" in out:
            sys.exit(f"unhandled PHP left in {page}")
        page.with_suffix(".html").write_text(fix_links(out), encoding="utf-8", errors="surrogateescape")

    # Static files that were already HTML/CSS may also carry /~russfeld/ paths or .php links.
    for f in list(ROOT.rglob("*.html")) + list(ROOT.rglob("*.css")):
        if "tools" in f.relative_to(ROOT).parts or f.relative_to(ROOT).as_posix() in INCLUDE_ONLY:
            continue
        text = f.read_text(encoding="utf-8", errors="surrogateescape")
        fixed = fix_links(text)
        if fixed != text:
            f.write_text(fixed, encoding="utf-8", errors="surrogateescape")

    for page in pages:
        page.unlink()
    for inc in INCLUDE_ONLY:
        (ROOT / inc).unlink()
    print(f"rendered {len(pages)} pages")


if __name__ == "__main__":
    main()
