"""Figura del capítulo 4 (sovieteconomy.tex) — edición en español.

Rótulos traducidos; los datos son los mismos que en ../english/figs/comecon.py
y cualquier corrección tiene que entrar en las dos versiones.

Two panels, both built only from figures traced to a source; nothing here is
interpolated between data points, which is why panel (a) is two bars rather
than a time series -- the price series for Soviet-Cuban sugar is not reliably
public year by year, and drawing a smooth line through two known values would
be inventing the shape.

(a) What the Soviet Union paid for Cuban sugar in 1987 against the world price
    that year. The ratio, not the level, is the subsidy.
(b) Sugar as a share of Cuban merchandise exports. The point of the panel is
    the flatness between 1958 and 1989: thirty years of planning, the highest
    investment rate in Latin America and a Comecon membership organised around
    international specialisation left the export basket where it started.
    Then it went to nothing.

Run: python3 figs/comecon.py   ->  figs/comecon.pdf
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 7.5,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.direction": "out",
    "ytick.direction": "out",
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(3.9, 1.85))

# --- (a) the price the subsidy was delivered through -----------------------
labels = ["Mercado\nmundial", "Pagado por\nla URSS"]
vals = [6.76, 41.9]                       # US cents per pound, 1987
bars = ax1.bar(labels, vals, width=0.55,
               color=["0.80", "0.35"], edgecolor="black", linewidth=0.6)
ax1.set_ylabel("centavos de dólar por libra")
ax1.set_ylim(0, 50)
ax1.set_title("(a) Precio del azúcar, 1987", fontsize=7.5, loc="left", pad=4)
for b, v in zip(bars, vals):
    ax1.text(b.get_x() + b.get_width() / 2, v + 1.4, f"{v:.1f}",
             ha="center", va="bottom", fontsize=7)
ax1.annotate("", xy=(1, 41.9), xytext=(0, 6.76),
             arrowprops=dict(arrowstyle="-", lw=0.5, ls=":", color="0.4"))
ax1.text(0.5, 26, r"$6.2\times$", ha="center", fontsize=7.5, style="italic")
ax1.spines[["top", "right"]].set_visible(False)

# --- (b) what thirty years of planning changed ------------------------------
years = [1958, 1970, 1980, 1989, 2000, 2010, 2023]
share = [80, 77, 84, 75, 30, 6, 0]        # per cent of merchandise exports
ax2.plot(years, share, marker="o", ms=2.8, lw=0.9, color="black")
ax2.set_ylim(0, 100)
ax2.set_xlim(1955, 2027)
ax2.set_ylabel("por ciento de las exportaciones")
ax2.set_title("(b) Peso del azúcar", fontsize=7.5, loc="left", pad=4)
ax2.axvspan(1958, 1989, color="0.90", zorder=0)
ax2.text(1973, 92, "era de la planificación", ha="center", fontsize=6.0,
         style="italic", color="0.35")
ax2.set_xticks([1958, 1989, 2023])
ax2.spines[["top", "right"]].set_visible(False)

fig.tight_layout(pad=0.4)
fig.savefig("figs/comecon.pdf", bbox_inches="tight")
print("escrito figs/comecon.pdf")
