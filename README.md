# A prospect of Cuba: Past and Future

A three-part book. Parts I and II report the history of Cuba 1959–1990 and
1990–2026 without taking a side — the good and the bad, in the same chapter, at
the same length. Part III is the point of the book: a proposed socio-political
and economic system for Cuba from 2026, built on the country's actual strengths
and answerable to the record the first two parts establish.

| | |
|---|---|
| [`english/`](english/) | **The primary edition.** Complete draft — 24 chapters, 232 pages. See [`english/README.md`](english/README.md) for the chapter table, the argument, and the rules the manuscript holds itself to. |
| [`spanish/`](spanish/) | Spanish edition. Complete draft — 24 chapters, 246 pages. Same chapter files, same design-box numbering; its own copy of `references.bib`, which must be kept identical to the English one. |

Build either edition with `latexmk -pdf main.tex` from inside its directory.
Each also carries an `ebook/` directory that produces a validated EPUB3 for
Kindle: `sh ebook/build-book.sh`.

## English is primary

Corrections of substance — a figure that turns out to be wrong, a claim that
does not survive checking, a design clause that changes — are made in
`english/` first and then carried into `spanish/`, never the other way round.

`english/verify.md` is the single verification ledger and covers **both**
editions. It is not mirrored into `spanish/`, deliberately: two copies of a list
of contested facts would diverge, and then the book would disagree with itself
in two languages. The Spanish text carries the same `\unv` marks at the same
claims, and `spanish/README.md` points at the English ledger.

`references.bib` is the exception, and the one file that *can* drift: each
edition holds a real copy. It used to be a symlink, which could not diverge; it
is now two files, which can. One line checks them:

```
cmp english/references.bib spanish/references.bib
```
