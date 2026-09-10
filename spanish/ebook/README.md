# Construcción EPUB / Kindle — *Una perspectiva de Cuba: Pasado y Futuro*

EPUB3 reflowable del libro completo (preliminares, tres partes, 24 capítulos,
bibliografía). Las fuentes de imprenta en `../` no se modifican nunca; todo lo
intermedio aquí se regenera a partir de ellas.

## Compilar

```sh
sh build-book.sh          # -> book-ebook.epub
epubcheck book-ebook.epub
```

Estado actual: **EPUBCheck 5.3 (EPUB 3.3), 0 errores / 0 advertencias**, 331 KB.

Requiere (todo viene con TeX Live): `tex4ebook`, `make4ht`, `pdflatex`, más
`perl`, `python3`, `pdftoppm` (poppler), `zip`/`unzip`. Validación: `epubcheck`.

## Qué cambia respecto de `../../english/ebook/`

El proceso es el mismo y los archivos de capítulo se llaman igual. Solo difieren:

- **`ebook-preamble.tex`** — añade `babel` en español, `T1` e `inputenc` (sin T1
  una palabra acentuada no se divide), y traduce los títulos de los dos
  recuadros: `Diseño N.M.` y `El balance:`.
- **`book-ebook.tex`** — título, y `\part{La perspectiva}`.
- **`build-book.sh`** — el título que se le pasa a `fixepub.py`.

`babel` fija por su cuenta `dc:language` y `lang` en `es`; no hay que tocarlos.

## La invariante que hay que revisar

**La numeración de los recuadros de diseño tiene que coincidir con la edición
inglesa**, porque la Parte III se remite a ellos por número. Se comprueba
mecánicamente comparando las dos copias descomprimidas:

```sh
grep -o 'class=.designbox.' OEBPS/*.xhtml | wc -l    # 52 en ambas
```

Hoy las dos ediciones producen los mismos 52 números, de 13.1 a 24.1.

La segunda invariante: **la conversión no debe generar imágenes propias.** Todas
las figuras se rasterizan a PNG antes de que corra tex4ebook, así que
`svg2png.py` debe informar `rasterised 0 images`. Si informa más, algo en las
fuentes empezó a producir dibujos y no va a fluir ni a escalar con la tipografía
del lector. Ocurrió una vez: el carácter `ș` (U+0219) de «Ceaușescu» salía como
una imagen de 7×13 px en mitad de la palabra; la fuente usa ahora `\c{s}`, igual
que la edición inglesa.

## Huecos conocidos

- **Sin imagen de cubierta.** KDP la exige; se aporta al subir.
- El `.ncx` heredado de EPUB2 omite algunas entradas de sección que el documento
  de navegación EPUB3 sí trae completas. Los lectores modernos, Kindle
  incluido, usan el de navegación; EPUBCheck pasa.
