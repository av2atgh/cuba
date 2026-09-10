#!/usr/bin/perl
# mkbody.pl PREFIX FILE  ->  preprocessed chapter body on stdout
#
# Prepares one print chapter for tex4ht. Far shorter than the equivalent in
# ~/av2atg/RunningMetabolism/ebook because this book has no display mathematics,
# no adjustbox and only three maths symbols in total.
#
# tex4ht cannot rasterise TikZ (its dvi driver does not run the pgf backend over
# the text nodes), so every tikzpicture is extracted to figures/<prefix>-N.tikz
# and replaced by \includegraphics; renderfigs.sh compiles those to PNG with the
# real TikZ engine via the standalone class.
use strict;
use warnings;

my $prefix = shift // 'fig';
local $/;
my $t = <>;

mkdir 'figures' unless -d 'figures';

# 1) The three maths symbols in the book, all in the energy table. As maths each
# becomes a small image: it does not reflow, does not scale with the reader's
# font, and cannot be searched. The preamble defines text equivalents.
$t =~ s/km\$\^2\$/\\sqkm/g;
$t =~ s/\$\\approx\$/\\approxsym/g;
$t =~ s/\$\\times\$/\\timessym/g;

# 2) matplotlib data figures: \includegraphics[..]{figs/NAME} -> figures/NAME.
# build-book.sh rasterises each ../figs/*.pdf to figures/NAME.png (EPUB readers
# do not render PDF); the width option is dropped because CSS handles sizing.
$t =~ s!\\includegraphics(?:\[[^\]]*\])?\{figs/([^}]+?)(?:\.pdf)?\}!\\includegraphics{figures/$1}!g;

# 3) inline tikzpictures -> figures/<prefix>-N.tikz + \includegraphics
my $n = 0;
$t =~ s/(\\begin\{tikzpicture\}.*?\\end\{tikzpicture\})/save_fig($prefix . '-' . (++$n), $1)/gse;

# 4) print-only navigation commands. \addcontentsline duplicates the front
# matter in the EPUB nav (tex4ebook already builds nav from the headings, so
# "Preface" appeared twice); \markboth sets running heads, which an EPUB has
# none of.
$t =~ s/\\addcontentsline\{[^{}]*\}\{[^{}]*\}\{(?:[^{}]|\{[^{}]*\})*\}//g;
$t =~ s/\\markboth\{(?:[^{}]|\{[^{}]*\})*\}\{(?:[^{}]|\{[^{}]*\})*\}//g;

# 5) any bare \input/\include of a sibling file -> resolve from ../
$t =~ s/\\(input|include)\{([^}\/]+)\}/\\$1\{..\/$2\}/g;

print $t;

sub save_fig {
    my ($name, $body) = @_;
    open my $fh, '>', "figures/$name.tikz" or die "figures/$name.tikz: $!";
    print $fh $body, "\n";
    close $fh;
    return "\\includegraphics{figures/$name}";
}
