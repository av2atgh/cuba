# EPUB / Kindle build — *A prospect of Cuba: Past and Future*

Reflowable **EPUB3** of the full book (front matter, three parts, 24 chapters,
bibliography). The print sources in `../` are never modified; every intermediate
here is regenerated from them.

## Build

```sh
sh build-book.sh          # -> book-ebook.epub
epubcheck book-ebook.epub
```

Current build: **EPUBCheck 5.3 (EPUB 3.3), 0 errors / 0 warnings**, 310 KB.

Requires (all ship with TeX Live): `tex4ebook`, `make4ht`, `pdflatex`, plus
`perl`, `python3`, `pdftoppm` (poppler), `zip`/`unzip`. Validation:
`epubcheck` (`brew install epubcheck`). `python3` needs Pillow.

## Why this is simpler than the RunningMetabolism build

That book is mostly equations; this one has **no display mathematics at all**
and exactly three maths symbols in the whole text, all in the energy table. So
the machinery that book needs — `align` restructuring, `split`→`aligned`,
per-equation SVG rasterisation, uniform display scaling — is absent here.
`mkbody.pl` is 40 lines rather than 145.

The consequence worth checking after any edit: **the conversion should generate
no images of its own.** Every figure is rasterised to PNG *before* tex4ebook
runs, so `svg2png.py` should report `rasterised 0 images`. If it reports more,
something in the sources has started producing pictures — most likely new maths
— and it will not reflow or scale with the reader's font.

## Pipeline (`build-book.sh`)

1. **`mkbody.pl ../<ch>.tex > <ch>-body.tex`** — preprocess each of the 24
   chapters plus the preface and the note on sources (see transforms below),
   extracting the one TikZ picture to `figures/*.tikz`.
2. **`renderfigs.sh`** — compile that TikZ figure to PNG through the
   `standalone` class; tex4ht cannot rasterise TikZ itself.
3. **`pdftoppm`** — rasterise the two matplotlib figures (`../figs/*.pdf`) to
   `figures/*.png` at 220 dpi. EPUB readers do not render PDF.
4. **`pdflatex` + `bibtex`** — generate `.aux`/`.bbl` so the 40 citations
   resolve.
5. **`tex4ebook -f epub3`** — convert.
6. **post-process** — `fixepub.py` merges `ebook.css` and fixes EPUB3 validity;
   `svg2png.py` rasterises any stray SVG (Kindle's KFX converter rejects SVG);
   repack.

## `mkbody.pl` transforms (why each exists)

- **three maths symbols → character entities.** `$\approx$`, `$\times$` and
  `km$^2$` would each become a small image: it would not reflow, would not scale
  with the reader's font, and could not be searched. They become `&#8776;`,
  `&#215;` and `km&#178;`.
- **`\includegraphics{figs/NAME}` → `figures/NAME`** — points at the rasterised
  PNG; the width option is dropped because CSS handles sizing.
- **TikZ extraction** — the one picture is written out for `renderfigs.sh`.
- **`\addcontentsline` and `\markboth` stripped** — tex4ebook builds the nav
  from the headings, so `\addcontentsline` put "Preface" in it twice; an EPUB
  has no running heads for `\markboth` to set.

## `ebook-preamble.tex`

Mirrors `../main.tex`, dropping what a reflowable book has no use for:
`geometry` (a 5×8 trim is meaningless), `fancyhdr` (no running heads or
folios), `makeidx` (a page-number index cannot work without pages — the
reader's own search is better), and `hyperref` (tex4ht makes its own links and
the two fight).

The two set-off boxes become CSS-styled `<div>`s rather than `tcolorbox`es, and
the clause list becomes a description list — in print `\rl` sets its label with
`\makebox`, which tex4ht turns into a picture. `<dt>`/`<dd>` is also the honest
markup: each clause is a term and its text.

**The design-box counter is shared with print and must stay that way.** Part III
cross-references all 52 boxes by number, so `\thedesign` is defined once, above
the `\ifdefined\HCode`. The EPUB currently has 52 design boxes and 11 ledger
boxes, matching the print book exactly; that is worth re-checking after edits:

```sh
grep -o 'class=.designbox.' OEBPS/*.xhtml | wc -l    # in an unzipped copy
```

## Known gaps

- **No cover image.** KDP requires one; supply it at upload, or add a cover
  page here if the book ever ships as a standalone EPUB.
- The legacy EPUB2 `.ncx` is missing a handful of section entries that the
  EPUB3 nav document has in full (193 links, all sections). Modern readers,
  Kindle included, use the nav document; EPUBCheck passes. Not worth chasing.
