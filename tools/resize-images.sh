#!/usr/bin/env bash
# Shrink PNG/JPEG images larger than 2000px on either side to fit within 2000x2000.
# Slides display them at ~600-850px, so this is visually lossless on screen.
# Only real files are touched; symlinked duplicates (tools/dedup.py) follow automatically.
# Print/download files are left at full resolution: everything in openhouse/files/
# and any image linked with href=. A resized file is kept only if smaller.
# Usage (repo root, needs ImageMagick):  tools/resize-images.sh
set -euo pipefail
cd "$(dirname "$0")/.."

find . -path ./.git -prune -o -path ./tools -prune -o -path ./openhouse/files -prune -o -type f \
     \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \) -print0 |
while IFS= read -r -d '' f; do
  read -r w h < <(identify -format '%w %h\n' "$f[0]" 2>/dev/null) || continue
  (( w > 2000 || h > 2000 )) || continue
  grep -rqE --include='*.html' "href=\"[^\"]*$(basename "$f")\"" . && continue
  tmp="$f.resize-tmp.${f##*.}"
  convert "$f[0]" -resize '2000x2000>' -quality 88 "$tmp"
  before=$(stat -c %s "$f"); after=$(stat -c %s "$tmp")
  if (( after < before )); then
    mv "$tmp" "$f"
    echo "resized ${w}x${h} $((before / 1024))K -> $((after / 1024))K  $f"
  else
    rm "$tmp"
  fi
done
