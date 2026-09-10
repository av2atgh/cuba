# Numbers not yet traced to a primary source

Every `\unv` in the manuscript is listed here. The macro prints nothing, so this
file is the only place the list exists; regenerate the raw locations with

    grep -n 'unv' *.tex | grep -v '^main.tex' | grep -v '^sources.tex'

Rule: a figure leaves this list only when it has been checked against a primary
or first-rank secondary source **and** the source is added to `references.bib`
and cited at the point of use. A figure that turns out to be contested does not
leave the list — it gets rewritten as a range with the disagreement named, per
the note on sources.

## Resolved — checked against a source, text updated

These left the list on 2026-09-09. Each is now cited in the manuscript.

| Claim | What the check changed | Source |
|---|---|---|
| LLECE 1997 education result | Confirmed and **strengthened**. 13 countries; Cuba ~350 on a scale with mean 250, SD 50 — so 2 SD holds. Carnoy's own framing is stronger than the book's was: pupils in Cuba's *lowest-income* schools outperformed most upper-middle-class pupils elsewhere in the region. Text now gives the scores, not just the SDs. | Carnoy 2007 |
| Special Period GDP fall | **Corrected.** 34.8% is 1989–93, not 1990–93. And it is the *lowest* figure in circulation, not the midpoint — Cuban media said 48%, independent reconstructions reach 50%. Text now says so and uses the official figure precisely because it is the most conservative. | Mesa-Lago & Pérez-López 2005 |
| Epidemic neuropathy | **Sharpened.** MINSAP counted 50,862 cases; epidemic ran 1991–94, peaking 1992–93; no deaths and <0.1% left with sequelae. Text updated on all three. | CDC MMWR 43(10), 1994 |
| Soviet subsidy magnitude | **Narrowed and improved.** The book said "a fifth to a third of national income"; the verified figure is ~23% over 1985–88. And there is now a hard price datum: 1987, USSR paid ~41.9¢/lb against a world price of 6.76¢ — 6.2×. Both are in the text and in Fig. 4.1. | CIA assessment; Mesa-Lago 2000 |
| Certified US expropriation claims | **Made exact.** 8,821 reports filed, 5,913 certified, $1.9bn principal, ~$9bn at the statutory 6% simple interest; only ~913 (15%) thought eligible for a Title III suit. | FCSC |
| 11 July 2021 detentions | **Corrected upward.** 1,481 deprived of liberty, of whom 57 under 18; ~600 prosecuted; ≥141 charged with sedition; sentences 4–30 years, not "up to 25". | Justicia 11J / Cubalex |
| Cuban population and exodus | **Made specific.** ONEI: 9.7m in 2024, down 1.4m in four years, census postponed. Independent: one study ~8m; Albizu-Campos ~1.79m departures 2021–24. | ONEI; Albizu-Campos |
| Cuban electricity output | **Added, and it matters.** 2023: 15.3 TWh generated, **3.7 TWh (~24%) lost in T&D**. Per-capita consumption 1,856 kWh (2018) → 1,387 (2023). The loss figure is now the lead argument in the energy chapter's "before anything is built" section. | IEA / lowcarbonpower |
| Cuban investment allocation | **Replaced a vague claim with the strongest numbers in the book.** 2024: tourism-related construction 37.4% of national investment, agriculture 2.7%, public health 2.0bn CUP against 11.9bn for hotels and restaurants. Monreal: agriculture 14× smaller than tourism. Reported as *shares*, which sidesteps the exchange-rate problem the book itself raised. | ONEI 2024, via Monreal |

## Still open

## 1. The inheritance (`inheritance.tex`) — 8

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Cuba 4th–5th in Latin America by income per head, 1958; TV sets per head; rail density | Mesa-Lago 2000 comparative tables; Pérez Jr. 2015 ch. 8; UN *Statistical Yearbook* 1957–58 |
| 2 | ~1 physician per 1,000; literacy 76% (1953 census); life expectancy ~62 | Censo de Población y Viviendas 1953; PAHO series |
| 3 | Agrupación Católica Universitaria 1956–57 rural survey (4% meat, 11% milk, 43% illiterate, ~60% earth floors, ~2% running water) | Original: *Encuesta de Trabajadores Rurales 1956–57*, pub. 1957. Trace the publication, not a citation of it |
| 4 | Sugar ≈ 80% of export earnings | ONEI historical series / Cuban Economic Research Project |
| 5 | 8% of farms hold ~70% of farmland (1946 census); US ownership 25–40% of milling capacity | Censo Agrícola Nacional 1946; the US-ownership range needs both endpoints sourced |
| 6 | Average unemployment ~16% in the mid-1950s | Consejo Nacional de Economía series; check the definition used |
| 7 | 20,000-dead figure's origin, and the 2,000–5,000 range | Trace the *Bohemia* January 1959 origin; range from Thomas 1971 and later scholarship |
| 8 | 1953 census: ~27% black or mixed race, and the undercount claim | de la Fuente 2001 |

## 2. Three years (`revolution.tex`) — 4

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | ~550 executions in 1959; the Cuba Archive totals | Both figures must be attributed to their producers, not merged |
| 2 | ~250,000 left 1959–62 | US INS admissions data; Eckstein 2003 |
| 3 | ~3,000 of ~6,000 physicians emigrated | Feinsilver 1993; check whether the base is 6,000 or 6,300 |
| 4 | Literacy campaign: ~707,000 taught, 23% → under 4% | Campaign's own final report; Carnoy 2007 for the later cohort evidence |

## 3. The social state (`socialstate.tex`) — 7

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Infant mortality 37–40 (late 1950s) → under 20 (mid-1970s) → single digits (1980s) | ONEI + PAHO; note the registration-coverage caveat explicitly |
| 2 | Life expectancy 62 → over 73 by mid-1980s | Same |
| 3 | 1997 UNESCO/LLECE result: Cuban 3rd–4th graders ~2 SD above regional mean; bottom-quartile Cubans above the regional average | Carnoy 2007 and the original LLECE report. **This is the load-bearing number for Part III — check it hardest** |
| 4 | Female labour-force participation 13% (1958) → over 30% (late 1970s) | ONEI; check the definition change |
| 5 | UMAP: 25,000–35,000 passed through, 1965–68 | No official count exists. Attribute the range |
| 6 | Political prisoners "tens of thousands" in the 1960s | Range and producer required, or the claim is softened |
| 7 | Freedom Flights ~300,000, 1965–73; Revolutionary Offensive 55,000–58,000 businesses | US State Dept / INS for the first; *Granma* March 1968 for the second |

## 4. The Soviet economy (`sovieteconomy.tex`) — 3

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Oil re-export among the largest sources of hard currency by the mid-1980s | Mesa-Lago; needs a year-by-year series, not a single assertion |
| 2 | Soviet support $4–6bn/yr in the 1980s, one fifth to one third of national income | The ruble conversion is the whole problem. State the method with the number |
| 3 | Sugar ~75% of exports in 1989 | ONEI 1989 |

## 5. Abroad (`internationalism.tex`) — 2

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | ~300,000 military and ~50,000 civilian Cubans served in Angola, 1975–91 | Gleijeses 2013 |
| 2 | Official count of 2,289 internationalist dead, published 1991 | *Granma* December 1989 / 1991 |

## 6. The Special Period (`collapse.tex`) — 9

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Imports $8.1bn (1989) → $2.2bn (1993) | ONEI/CEPAL trade series; state the year-by-year path, not just endpoints |
| 2 | Oil imports ~13 Mt → ~6 Mt | ONEI energy balance |
| 3 | GDP −34.8% official, independent reconstructions 35–40% | Mesa-Lago; CEPAL *Cuba: evolución económica*. Say which convention each uses |
| 4 | Caloric intake ~2,900 (1989) → ~1,860 kcal/day (1993); protein down ~half | FAO food balance sheets + Cuban national nutrition survey |
| 5 | Epidemic neuropathy ~50,000 cases 1992–93 | MINSAP/PAHO reports; *NEJM* and *Lancet* papers of 1993–95 |
| 6 | Infant mortality 11.1 (1989) → under 10 (1994), falling throughout | ONEI + PAHO. **Load-bearing for the welfare argument — check hardest** |
| 7 | Diabetes/CVD mortality fell with the weight loss and rose again after 1995 | Franco et al., *BMJ* 2013, and the earlier *Am J Epidemiol* paper |
| 8 | *13 de Marzo* tugboat: 37 dead, 10 children, 13 July 1994 | IACHR Report 47/96 |
| 9 | Balseros: 30,000–35,000 in five weeks, Aug–Sep 1994 | US Coast Guard interdiction statistics |

## 7. Reform and reversal (`dollarreform.tex`) — 6

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | UBPCs took ~40% of agricultural land (1993) | ONEI land-tenure series; check whether the share is of arable or of total |
| 2 | Deficit ~30% of output (1993) → 7% (1994) → 2% (1996); informal rate 150 → 25 | Banco Central de Cuba; Mesa-Lago. The best-documented Cuban stabilisation and the precedent `money` leans on |
| 3 | Gini ~0.24 (mid-1980s) → ~0.40 (late 1990s) | Ferriol Muruaga / INIE household studies. Note the coverage caveat |
| 4 | ≥80% of remittances reaching white households | de la Fuente; Blue; Eckstein. Attribute the survey, do not average them |
| 5 | Tourist arrivals 340k (1990) → 745k (1995) → 1.8m (2000) | ONEI tourism series |
| 6 | Self-employment ~209,000 (early 1996) → ~150,000 (2003) | ONEI employment series; Ritter & Henken 2015 |

## 8. The Venezuelan decade (`venezuela.tex`) — 7

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Oil 53,000 bpd (2000) rising to ~90–100,000 bpd | The 2000 Convenio text; PDVSA reporting |
| 2 | 20,000–30,000 Cuban health workers; ~40,000 total Cuban personnel in Venezuela | Ranges only; attribute the producers |
| 3 | Professional-service exports $8–10bn/yr vs tourism ~$2.5bn, nickel ~$1.5bn | ONEI balance of payments. This is the chapter's central fact — source it precisely |
| 4 | Cuba received ~4× what it passed to the physician (Mais Médicos) | PAHO/Brazilian federal contracts, which are public |
| 5 | Energy Revolution 2006: ~9m bulbs, ~4,000 gensets, ~1,300 MW | MINEM/Granma contemporaneous reporting. Load-bearing for `energy` |
| 6 | 2008 hurricanes: >500,000 homes, ~$10bn, ~20% of GDP | CEPAL damage assessment |
| 7 | 2009 freeze of foreign accounts >$1bn | Reuters/EIU contemporaneous; no official figure exists — say so |

## 9. Raúl's decade (`raul.tex`) — 4

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | 2010 consultation: ~160,000 meetings, ~two thirds of paragraphs modified | The Lineamientos' own published *Información sobre el resultado del Debate* |
| 2 | Self-employed 157,000 (2010) → >500,000 (2015), ~a fifth of the workforce | ONEI employment series |
| 3 | >1.7m hectares granted in usufruct under DL 259/300 | ONEI agriculture; check whether granted or actually occupied — the gap is the point |
| 4 | US visitors 91,000 (2014) → >600,000 (2017), excluding Cuban-Americans | ONEI vs US Dept of Commerce; the two count differently |

## 10. The crisis (`crisis.tex`) — 17

**Every figure in this chapter from 2023 onward is provisional.** The chapter
says so in its first section; the check is to re-source them all against
whatever ONEI, ONU-CEPAL and the independent Cuban economists have published
since, and to update the text rather than leave the hedges standing.

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | "243 measures" 2017–20 | The count is a advocacy-group tally; attribute it or drop it |
| 2 | Tourism 4.7m (2018) → 1.1m (2020) → <400k (2021) → ~2.4m (2023), stalling since | ONEI |
| 3 | Cuba's divergence from full Caribbean tourism recovery | CTO regional arrivals data — needed to support the causal claim |
| 4 | Vaccine efficacies >90%; >90% population coverage; from age two | The Cuban trial publications and their peer-reviewed status. State what was and was not peer-reviewed |
| 5 | GDP −11% in 2020 | ONEI/CEPAL |
| 6 | Official CPI ~77% (2021) and high double digits after | ONEI; note that the official index excludes much of what households buy |
| 7 | Informal rate >100 (2022), >200 (2023), >300 (2024) | *El Toque* series, which is the only continuous one — attribute it as such |
| 8 | 11J: 40–60+ locations | Cubalex / Justicia 11J / ACI |
| 9 | 11J: 1,300–1,500 detained, several hundred prosecuted, sentences to 25 years, minors convicted | Justicia 11J and Prisoners Defenders; these are the only counts and must be named as opposition monitors |
| 10 | MSMEs: ~11–12,000 approved by 2024, mostly private | MEP published register |
| 11 | Grid: national collapses Oct/Nov/Dec 2024 and 2025 | UNE daily reports; confirm the 2025 events individually |
| 12 | Chinese solar: ~1,000 MW target, several hundred MW energised in 2025 | UNE/MINEM. **Load-bearing for `energy` — get the actual installed and delivered figures** |
| 13 | US encounters: ~220,000 (FY2022), ~200,000 (FY2023); parole programme volumes | CBP nationwide encounters data |
| 14 | Total departures 2021–25 of 1–2 million | A range, not a figure. Name Albizu-Campos and the ONEI position separately |
| 15 | Resident population below 10m (ONEI 2024) vs 8.5–9.5m (independent demographers) | Report the disagreement, do not split it |
| 16 | TFR ~1.2–1.4; >25% over sixty | ONEI demographic yearbook |
| 17 | Sugar in the low hundreds of thousands of tonnes; Cuba importing sugar; WFP milk assistance 2023 | AZCUBA; WFP country reports |

## 11. The balance sheet (`ledgerch.tex`) — 2

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Food imports two thirds to four fifths of consumption | The range is wide because the denominator varies (calories? value? volume?). Fix the denominator and the figure narrows |
| 2 | TFR ~1.2–1.4 by the mid-2020s | Same source as `crisis` #16; keep the two chapters consistent |

---

# Part III

Part III's figures are of a different kind from Parts I and II. They are not
historical claims but **design inputs** — order-of-magnitude engineering and
fiscal estimates whose assumptions are stated on the page. The check is
therefore different too: not "did this happen?" but "is this assumption still
right, and does the conclusion survive changing it?"

Two of them are load-bearing for the book's central argument and should be
re-derived properly rather than merely sourced.

## 14. The social contract (`welfare.tex`) — 1

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | EU norms: social spending 25–30% of GDP; health 7–8%, education ~5%, pensions 10–12%; total government 40–50%; tax revenue 35–45% | Eurostat COFOG and OECD Revenue Statistics. Give the year and the country spread, not a single band |

## 15. Money (`money.tex`) — 1

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Certified US claims: ~5,900, ~$1.9bn principal (early 1970s), several times that with interest | US Foreign Claims Settlement Commission final decisions. State the interest convention explicitly — it is where most of the disagreement lives |

## 16. Sun (`energy.tex`) — 3 — **load-bearing**

The arithmetic table is the strongest quantitative argument in the book and it
must be redone properly, not merely checked.

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | ~20 TWh/yr generation, 3,000–3,300 MW peak, ~30% fleet efficiency, ~6 Mt/yr fuel oil equivalent | ONEI energy balance and UNE. Also get the actual hourly load shape — the storage sizing depends on the evening peak's width, which is assumed here |
| 2 | GHI 5.0–5.5 kWh/m²/day; specific yield 1,500–1,700 kWh/kWp/yr | Run PVGIS or Solargis for several Cuban sites rather than quoting a range. Include the temperature and soiling derates explicitly |
| 3 | $0.80/Wp installed, $200/kWh storage, 1.5 ha/MWp, $400–500/t fuel | Delivered island cost, not global average — freight, insurance and the embargo premium are real. Get a quote-based figure if possible |

**What would change the conclusion:** installed cost above ~$1.4/Wp, or specific
yield below ~1,200 kWh/kWp/yr, would push simple payback past a decade and
weaken the case materially. Neither is likely; both should be checked.

## 17. Visitors (`tourism.tex`) — 2

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Hotel construction as the largest line in gross fixed capital formation, several times agriculture's share, with occupancy in the 20s–30s | ONEI investment by activity, and hotel occupancy series. **This is the book's worked example of capital misallocation — source it precisely, year by year** |
| 2 | All-inclusive leakage: a fifth to a third retained | UNWTO/UNCTAD Caribbean leakage literature. The range is wide and methodology-dependent; say whose method |

## 18. The second track (`talent.tex`) — 1 — **load-bearing**

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | 100,000 workers × $18,000/yr ≈ $1.8bn | The multiplication is trivial; the assumptions are not. Check both against actual remote-services earnings in comparable markets (Uruguay, Argentina, Colombia, Philippines) and against the realistic supply of Cuban workers with the skills, given the emigration in `crisis`. If either input is off by half, the sector is a third the size claimed — still worth building, but say so |

## 19. Life sciences (`life.tex`) — 2

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Product claims: first meningococcal B vaccine; first synthetic-antigen vaccine in routine use (Quimi-Hib); COVID vaccines with >90% coverage | Verify each priority claim individually against the primary literature — these are the sector's reputation and one wrong "first" discredits the rest |
| 2 | Pharma exports a few hundred $m/yr vs medical services 20–30× larger at peak | ONEI balance of payments, disaggregated. The ratio is the chapter's whole argument |

## 20. Land and food (`land.tex`) — 2

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | 1–2m ha under marabú | Widely repeated, rarely sourced. Look for remote-sensing work rather than a ministry statement |
| 2 | Post-harvest losses of a fifth to a third | FAO and Cuban agricultural ministry estimates. Perishables vs staples differ greatly — disaggregate |

## 21. Capital and property (`capital.tex`) — 1

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | Housing deficit in the hundreds of thousands of units | ONEI housing statistics and the ministry's own acknowledgements. Definitions vary enormously (deficit vs. units in poor condition) — fix the definition |

## 24. The sequence (`sequence.tex`) — 1 — **load-bearing**

| # | Claim | Where to check |
|---|-------|----------------|
| 1 | The whole costs-and-sources table, and in particular hotel construction at ~$1–1.5bn/yr redirectable | The claim that Cuba can fund its energy transition out of its own misallocated investment budget is the book's most important financing argument. It rests on the hotel investment figure in `tourism` #1. If that figure is materially smaller, this argument weakens and the financing has to come from somewhere named |


---

# Figure data

Figures are generated by scripts in `figs/` and re-run with
`python3 figs/<name>.py`. Two of the three carry data that is not fully sourced,
and the captions say so on the page.

| Figure | Element | Status |
|---|---|---|
| 4.1(a) Sugar price 1987 | 41.9¢ vs 6.76¢/lb | **Sourced.** Deliberately two bars, not a series — the year-by-year Soviet–Cuban price data is not reliably public, and drawing a line through two known points would invent the shape |
| 4.1(b) Sugar's share of exports | 1958–1989 values | Consistent with the text and with ONEI; check each point |
| 4.1(b) | 2000, 2010, 2023 values | **Estimated.** ~30%, ~6%, ~0%. Derived, not read off a table. Verify against ONEI trade series |
| 16.1(a) Daily load shape | The curve itself | **Schematic, and labelled as such in the caption.** Cuba's actual hourly demand curve is not reliably public. Obtaining it is the single highest-value check remaining in the book — the storage sizing in the chapter's table depends on the width of the evening peak, which is currently assumed |
| 16.1(a) | The qualitative claim (peak after sunset) | Not in doubt |
| 16.1(b) Payback sensitivity | The curves | Derived from the chapter's own stated assumptions, so it is internally consistent by construction. Its value is that it shows the break-point: past roughly $1.50/Wp the ten-year payback fails across the whole plausible yield range |
| 24.1 Phase timeline | — | No data; it is a schematic of the chapter's ordering claims |
