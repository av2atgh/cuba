# A prospect of Cuba — Spanish edition

Not started.

The English manuscript in [`../english/`](../english/) is the source text: 24
chapters, complete draft. When this edition begins, the things worth deciding
first, because they are expensive to change later:

- **Translation or re-writing.** The book's primary audience is arguably Cuban
  and in Cuba, which is an argument for the Spanish edition being the one
  written *for* its reader rather than a translation of one written for someone
  else. Part III in particular addresses Cubans about Cuban institutions.
- **Terms that should not be translated back through English.** The manuscript
  uses *acopio*, *libreta*, *cuentapropismo*, *jineterismo*, *marabú*,
  *parametración*, *paladar*, *casa particular*, *maleconazo*, *quinquenio
  gris*, *acto de repudio*, *resolver*, *luchar*, *tarjeta blanca*,
  *pedraplén*, *bohío*, *tiempo muerto*, *zafra*. In Spanish these stop being
  glossed foreign words and become the ordinary vocabulary, which changes how
  several passages have to be written.
- **Register.** The English text explains Cuban institutions to a reader who does
  not know them. A Cuban reader does. Passages that exist only to explain
  *acopio* or the *libreta* should shrink; passages that argue about what to do
  about them should not.
- **What must not drift.** The design boxes in Part III are numbered
  institutional rules and are cross-referenced by number throughout. If the
  editions diverge in their numbering they stop being the same book.
- **The verification ledger.** [`../english/verify.md`](../english/verify.md)
  tracks every figure not traced to a primary source. Corrections must land in
  both editions or the two will disagree on facts.

Production follows the English edition: 5×8 in trim, 10pt, grayscale, one file
per chapter. Spanish needs `\usepackage[spanish]{babel}` and its hyphenation
patterns, and the running heads and the `design`/`ledger` box titles will need
translating in the preamble rather than per chapter.
