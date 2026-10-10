# archive.russfeld.me

Archive of Russell Feldhausen's course and outreach materials from 2013–2018
(originally hosted at people.cs.ksu.edu/~russfeld), preserved as they were.
The current site is [russfeld.me](https://russfeld.me).

- Pages were pre-rendered once from the original PHP (includes only) to static
  HTML with `tools/render-php.py`; that script is kept for provenance and is
  not part of the build.
- `tools/fix-links.py` (one-time) repaired internal links that were already broken in
  the original (copied decks with the wrong `<BASE>`, missing image extensions, etc.).
- Duplicate files are relative symlinks to a single copy (`tools/dedup.py`, safe to
  re-run after adding content). Images over 2000px were shrunk with
  `tools/resize-images.sh`; open house print templates are kept at full resolution.
- Google Analytics 4: the measurement ID lives only in `js/analytics.js`.
- Served as static files by `nginx:alpine` (see `Dockerfile`, `nginx/default.conf`).
  Pushes to `main` build `ghcr.io/russfeld/archive:latest` and trigger Watchtower.
