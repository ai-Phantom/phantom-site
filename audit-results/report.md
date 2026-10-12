# Live audit + feature test — https://aiphantomtraders.com

2026-10-12T22:00:50.515Z → 2026-10-12T22:02:48.318Z

## Findings

- **HIGH** — No /market/quote response observed — backend likely cold (Render free tier).

## Source-code leak (visible raw code on page)

_No raw source detected in visible text._

## Feature click-test errors

_No errors thrown while clicking tabs / dropdowns / FAQ / CTAs._


## Live ticker (homepage grid + tape)

Clock `MARKET · 22:01:00 ET`

| Symbol | Grid % | Tape px |
|---|---:|---:|
| SPY | −0.06% | 778.10 |
| QQQ | −0.70% | 746.04 |
| IWM | −0.37% | 277.90 |
| NVDA | −1.29% | 226.32 |
| TSLA | −1.22% | 378.03 |
| AAPL | +1.29% | 340.97 |
| MSFT | +1.14% | 541.15 |
| AMZN | −1.11% | 259.53 |
| META | +3.38% | 742.96 |
| GOOGL | +0.30% | 352.72 |
| AMD | −2.28% | 594.24 |
| NFLX | +0.44% | 70.61 |
| COIN | +0.56% | 180.39 |
| PLTR | −0.02% | 209.00 |
| MSTR | −1.08% | 152.68 |
| SMCI | −4.48% | 39.98 |
| CRWD | −4.37% | 263.01 |
| ORCL | · | — |
| UBER | −0.01% | 71.50 |
| PYPL | +0.94% | 56.05 |
| MARA | −2.18% | 9.44 |
| RIOT | −2.46% | 16.47 |
| HOOD | +0.18% | 109.22 |
| SOFI | −3.61% | 15.23 |
| BAC | +0.48% | 54.58 |
| INTC | −3.20% | 101.35 |
| DIS | +0.41% | 108.49 |
| SNAP | +4.82% | 6.53 |
| LYFT | −0.68% | 16.11 |
| TGT | −0.01% | 153.62 |
| NKE | +1.84% | 35.35 |
| COF | +0.94% | 201.14 |

## Market API

_no /market/quote call observed_

## Pages

| Page | Viewport | HTTP | OK | Console errs |
|---|---|---|---|---|
| home | desktop | 200 | ✅ | 0 |
| home | mobile | 200 | ✅ | 0 |
| features | desktop | 200 | ✅ | 0 |
| features | mobile | 200 | ✅ | 0 |
| pricing | desktop | 200 | ✅ | 0 |
| pricing | mobile | 200 | ✅ | 0 |
| products | desktop | 200 | ✅ | 0 |
| products | mobile | 200 | ✅ | 0 |
| blog | desktop | 200 | ✅ | 0 |
| blog | mobile | 200 | ✅ | 0 |
| discord | desktop | 200 | ✅ | 0 |
| discord | mobile | 200 | ✅ | 0 |
| dashboard | desktop | 200 | ✅ | 0 |
| dashboard | mobile | 200 | ✅ | 0 |
| signup | desktop | 200 | ✅ | 0 |
| signup | mobile | 200 | ✅ | 0 |
| legal | desktop | 200 | ✅ | 0 |
| legal | mobile | 200 | ✅ | 0 |
| docs | desktop | 200 | ✅ | 0 |
| docs | mobile | 200 | ✅ | 0 |
| store | desktop | 200 | ✅ | 0 |
| store | mobile | 200 | ✅ | 0 |