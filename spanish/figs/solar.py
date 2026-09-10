"""Figura del capítulo 16 (energy.tex) — edición en español.

Rótulos traducidos; los datos y los supuestos son los mismos que en
../english/figs/solar.py y cualquier corrección tiene que entrar en ambas.

(a) Why storage is not optional. The daily load shape is SCHEMATIC -- Cuba's
    actual hourly demand curve is not reliably public, and verify.md records
    that obtaining it is the first thing that should be done to this chapter.
    What is not schematic is the qualitative fact the panel exists to show:
    Cuban demand peaks after sunset, so photovoltaic capacity alone displaces
    midday fuel -- the cheapest fuel to displace -- and leaves the hours that
    determine whether the grid holds exactly as they were.

(b) The sensitivity the argument actually turns on. Simple payback against
    installed cost, at three specific yields spanning the plausible Cuban
    range. The horizontal line is a ten-year payback, taken as the point past
    which the case weakens materially. The vertical marks the $0.80/Wp used in
    the chapter's table.

Run: python3 figs/solar.py   ->  figs/solar.pdf
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 7.5,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(3.9, 1.9))

# --- (a) the evening gap ----------------------------------------------------
h = np.linspace(0, 24, 481)
# schematic load: overnight trough, mild midday shoulder, sharp evening peak
load = (0.58
        + 0.16 * np.exp(-((h - 12.5) ** 2) / (2 * 3.0 ** 2))
        + 0.42 * np.exp(-((h - 19.5) ** 2) / (2 * 1.7 ** 2)))
# PV: sunrise ~0630, sunset ~1900, clipped cosine bell
pv = np.clip(np.cos((h - 12.9) / 6.4 * (np.pi / 2)), 0, None) ** 1.35
pv = pv / pv.max() * 0.95

ax1.plot(h, load, color="black", lw=1.0, label="demanda")
ax1.plot(h, pv, color="0.45", lw=1.0, ls="--", label="salida FV")
gap = (h > 17.0) & (h < 23.5)
ax1.fill_between(h[gap], np.minimum(load, pv)[gap], load[gap],
                 color="0.75", alpha=0.85, lw=0)
ax1.text(20.2, 0.40, "el almacenamiento\ntiene que cubrir\nesto", ha="center", va="center",
         fontsize=6.2, style="italic")
ax1.set_xlim(0, 24); ax1.set_ylim(0, 1.15)
ax1.set_xticks([0, 6, 12, 18, 24])
ax1.set_xlabel("hora")
ax1.set_ylabel("normalizado")
ax1.set_title("(a) El pico de la noche", fontsize=7.5, loc="left", pad=4)
ax1.legend(frameon=False, fontsize=6.2, loc="upper left",
           handlelength=1.4, borderpad=0.1)
ax1.spines[["top", "right"]].set_visible(False)

# --- (b) payback sensitivity ------------------------------------------------
# 10 TWh/yr target; fuel displaced at 30% thermal efficiency, 40 GJ/t,
# valued at $450/t. Storage held at the chapter's $1.6bn.
cost = np.linspace(0.4, 2.0, 200)          # $/Wp installed
fuel_saving = 1.35e9                        # $/yr, chapter's midpoint
storage = 1.6e9
for yld, style, lab in [(1300, ":", "1,300"), (1600, "-", "1,600"), (1900, "--", "1,900")]:
    gwp = 10e9 / yld                        # kWp required
    capex = gwp * 1e3 * cost + storage      # $/Wp -> $/kWp
    ax2.plot(cost, capex / fuel_saving, style, color="black", lw=0.9, label=lab)
ax2.axhline(10, color="0.55", lw=0.6)
ax2.text(1.92, 10.5, "10 años", ha="right", fontsize=6.2, color="0.4")
ax2.axvline(0.80, color="0.55", lw=0.6, ls=":")
ax2.text(0.86, 1.0, "supuesto del\ncapítulo", fontsize=6.0, color="0.4")
ax2.set_xlabel("costo instalado, \\$/Wp")
ax2.set_ylabel("recuperación simple, años")
ax2.set_xlim(0.4, 2.0); ax2.set_ylim(0, 23)
ax2.set_title("(b) Qué lo rompería", fontsize=7.5, loc="left", pad=4)
ax2.legend(frameon=False, fontsize=6.2, title="kWh/kWp/yr",
           title_fontsize=6.2, loc="lower right", handlelength=1.6,
           borderpad=0.1, labelspacing=0.25)
ax2.spines[["top", "right"]].set_visible(False)

fig.tight_layout(pad=0.4)
fig.savefig("figs/solar.pdf", bbox_inches="tight")
print("escrito figs/solar.pdf")
