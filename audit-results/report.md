# Live audit + feature test — http://localhost:8080

2026-06-23T18:23:17.028Z → 2026-06-23T18:26:59.012Z

## Findings

- **HIGH** — No /market/quote response observed — backend likely cold (Render free tier).

## Source-code leak (visible raw code on page)

_No raw source detected in visible text._

## Feature click-test errors

_No errors thrown while clicking tabs / dropdowns / FAQ / CTAs._


## Live ticker (homepage grid + tape)

Clock `MARKET · 18:23:26 ET`

| Symbol | Grid % | Tape px |
|---|---:|---:|
| SPY | −1.22% | 735.28 |
| QQQ | −3.02% | 715.66 |
| IWM | −0.83% | 295.70 |
| NVDA | −3.36% | 201.64 |
| TSLA | −5.98% | 380.82 |
| AAPL | +0.52% | 298.54 |
| MSFT | +1.72% | 373.66 |
| AMZN | +1.04% | 235.22 |
| META | −0.12% | 563.18 |
| GOOGL | −0.98% | 346.24 |
| AMD | −5.82% | 519.53 |
| NFLX | +0.59% | 73.31 |
| COIN | −3.59% | 158.93 |
| PLTR | −1.18% | 118.09 |
| MSTR | −4.19% | 104.87 |
| SMCI | −5.84% | 33.39 |
| CRWD | +1.57% | 686.04 |
| ORCL | −3.18% | 172.14 |
| UBER | −0.03% | 77.47 |
| PYPL | −1.39% | 41.75 |
| MARA | +0.20% | 14.88 |
| RIOT | +0.77% | 28.85 |
| HOOD | −1.95% | 103.65 |
| SOFI | +1.35% | 17.33 |
| BAC | +0.68% | 57.76 |
| INTC | −5.87% | 132.66 |
| DIS | +0.88% | 103.35 |
| SNAP | −2.59% | 4.51 |
| LYFT | −1.34% | 14.03 |
| TGT | +3.47% | 134.23 |
| NKE | −1.00% | 42.76 |
| COF | −1.71% | 197.26 |

## Market API

_no /market/quote call observed_

## Pages

| Page | Viewport | HTTP | OK | Console errs |
|---|---|---|---|---|
| home | desktop | 200 | ✅ | 2 |
| home | mobile | 200 | ✅ | 2 |
| features | desktop | 200 | ✅ | 2 |
| features | mobile | 200 | ✅ | 2 |
| pricing | desktop | 200 | ✅ | 2 |
| pricing | mobile | 200 | ✅ | 2 |
| products | desktop | 200 | ✅ | 2 |
| products | mobile | 200 | ✅ | 2 |
| blog | desktop | 200 | ✅ | 2 |
| blog | mobile | 200 | ✅ | 2 |
| discord | desktop | 200 | ✅ | 2 |
| discord | mobile | 200 | ✅ | 2 |
| dashboard | desktop | 200 | ✅ | 2 |
| dashboard | mobile | 200 | ✅ | 2 |
| signup | desktop | 200 | ✅ | 2 |
| signup | mobile | 200 | ✅ | 2 |
| legal | desktop | 200 | ✅ | 2 |
| legal | mobile | 200 | ✅ | 2 |
| docs | desktop | 200 | ✅ | 2 |
| docs | mobile | 200 | ✅ | 2 |
| store | desktop | 200 | ✅ | 2 |
| store | mobile | 200 | ✅ | 2 |