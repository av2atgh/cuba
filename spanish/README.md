# Una perspectiva de Cuba: Pasado y Futuro — edición en español

Traducción de la edición inglesa en [`../english/`](../english/). Borrador
completo: 24 capítulos, 246 páginas, 52 recuadros de diseño numerados, 3 figuras.
Compila con 0 errores, 0 referencias no definidas, 0 cajas desbordadas
horizontales y 0 verticales.

## El lector

La decisión que gobierna todo lo demás. El lector de esta edición **no es
necesariamente cubano**. Es hispanohablante, y puede ser mexicano, argentino,
español o colombiano. Sabe lo que significa la palabra *libreta*; no sabe que en
Cuba nombra una cartilla de racionamiento vigente desde 1962. Conoce la palabra
*acopio*; no conoce el monopsonio estatal que lleva ese nombre.

De ahí las dos reglas del vocabulario, que no son la misma:

- **Los términos cubanos no se traducen.** Ya están en español. *Acopio*,
  *libreta*, *cuentapropismo*, *jineterismo*, *marabú*, *parametración*,
  *paladar*, *casa particular*, *maleconazo*, *quinquenio gris*, *acto de
  repudio*, *resolver*, *luchar*, *tarjeta blanca*, *pedraplén*, *bohío*,
  *tiempo muerto*, *zafra*, *balsero*, *gusano*, *microbrigada*.
- **Pero se siguen explicando.** La edición inglesa glosa cada uno porque su
  lector no conoce la palabra. Esta edición los glosa porque su lector conoce la
  palabra y no la institución. La glosa cambia de forma, no desaparece.

Un lector cubano encontrará explicado lo que ya sabe. Es el precio correcto: el
libro no está escrito solamente para cubanos, y la Parte III propone un sistema
que a otros países de la región les concierne por comparación.

## Lo que no puede divergir

- **La numeración de los recuadros de diseño.** La Parte III se remite a ellos
  por número a lo largo de todo el libro. Si las dos ediciones numeran distinto
  dejan de ser el mismo libro. Los archivos llevan los mismos nombres que en
  `english/` y las cajas aparecen en el mismo orden, precisamente por esto.
- **Los hechos.** La edición inglesa es la primaria.
  [`../english/verify.md`](../english/verify.md) es el único registro de
  verificación y cubre las dos ediciones: recoge cada cifra no rastreada hasta
  una fuente primaria, y anota qué cambió cada comprobación ya hecha. No se
  duplica aquí a propósito ---dos copias de una lista de hechos en disputa
  acabarían divergiendo, y entonces el libro se contradiría a sí mismo en dos
  idiomas---. Este texto lleva las mismas marcas `\unv` en las mismas
  afirmaciones. Las correcciones de fondo se hacen primero en `english/` y
  después se trasladan aquí, nunca al revés.
- **La bibliografía.** Cada edición tiene su propia copia de `references.bib`.
  Antes eran un enlace simbólico, que no podía separarse; ahora son dos archivos
  reales y sí pueden. Comprobarlo es una línea:
  `cmp ../english/references.bib references.bib`.

`summary.md` recoge el argumento del libro en menos de 200 palabras.

`ebook/` contiene la construcción EPUB3 / Kindle: `sh ebook/build-book.sh`
produce `book-ebook.epub` a partir de estas mismas fuentes sin tocarlas.

## Producción

Sigue a la edición inglesa: formato 5×8 pulgadas, 10pt, escala de grises, un
archivo por capítulo. Añade `babel` en español, codificación T1 para que las
palabras acentuadas se dividan bien, y los títulos de los recuadros traducidos
en el preámbulo. Las figuras se regeneran con `python3 figs/<nombre>.py`; son
versiones propias, con los rótulos en español.

Compilar con `latexmk -pdf main.tex`.
