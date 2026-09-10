#!/bin/sh
# build-book.sh — full-book EPUB3 (front matter + 24 chapters, 3 parts).
# Print sources in ../ are never modified.
set -e
cd "$(dirname "$0")"

# `sh build-book.sh clean` removes every generated file and nothing else.
# book-ebook.tex is a SOURCE despite matching book-ebook.*, so a glob delete
# takes it out along with the artifacts -- easy to do, confusing to diagnose.
if [ "$1" = clean ]; then
  rm -rf figures book-ebook-epub3 META-INF OEBPS
  rm -f -- *-body.tex book-ebook*.xhtml book-ebook*.svg book-ebook-*.dlog \
        content.opf mimetype _figwrap.tex *.4ct *.4tc
  for f in book-ebook.*; do
    [ "$f" = book-ebook.tex ] || rm -f -- "$f"
  done
  echo "cleaned (book-ebook.tex kept: it is a source, not an artifact)"
  exit 0
fi

FRONT="preface sources"
CHAPTERS="inheritance revolution socialstate sovieteconomy internationalism \
collapse dollarreform venezuela raul crisis ledgerch \
premises polity welfare money energy tourism talent life land capital \
integrity nature sequence"

echo ">> 1/6  preprocessing front matter and chapters -> *-body.tex"
rm -rf figures
for ch in $FRONT $CHAPTERS; do
  perl mkbody.pl "$ch" "../$ch.tex" > "$ch-body.tex"
done

echo ">> 2/6  rendering extracted TikZ figures -> PNG (standalone)"
sh renderfigs.sh

echo ">> 3/6  rasterising data figures (../figs/*.pdf) -> figures/*.png"
mkdir -p figures
for pdf in ../figs/*.pdf; do
  [ -e "$pdf" ] || continue
  name=$(basename "${pdf%.pdf}")
  pdftoppm -png -r 220 -singlefile "$pdf" "figures/$name" \
    && echo "  rasterised $name.png"
done

echo ">> 4/6  generating .aux/.bbl so citations resolve"
pdflatex -interaction=nonstopmode book-ebook.tex >/dev/null 2>&1 || true
bibtex book-ebook >/dev/null 2>&1 || true

echo ">> 5/6  tex4ebook -> EPUB3"
tex4ebook -f epub3 -c ebook.cfg book-ebook.tex

echo ">> 6/6  post-process: merge CSS, fix EPUB3 validity, SVG->PNG, repack"
out="$PWD/book-ebook.epub"
tmp="$(mktemp -d)"
unzip -q "$out" -d "$tmp"
python3 fixepub.py "$tmp" ebook.css "Una perspectiva de Cuba: Pasado y Futuro"
python3 svg2png.py "$tmp"
rm -f "$out"
( cd "$tmp" && zip -X -q -0 "$out" mimetype && zip -X -q -9 -r "$out" . -x mimetype )
rm -rf "$tmp"

echo ">> done: $(ls -1 book-ebook.epub 2>/dev/null || echo 'EPUB NOT PRODUCED')"
