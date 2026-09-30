# Live audit + feature test — https://aiphantomtraders.com

2026-09-30T23:04:19.167Z → 2026-09-30T23:06:37.793Z

## Findings

- **HIGH** — No /market/quote response observed — backend likely cold (Render free tier).

## Source-code leak (visible raw code on page)

_No raw source detected in visible text._

## Feature click-test errors

_No errors thrown while clicking tabs / dropdowns / FAQ / CTAs._


## Live ticker (homepage grid + tape)

Clock `MARKET · 23:04:29 ET`

| Symbol | Grid % | Tape px |
|---|---:|---:|
| SPY | −0.21% | 762.63 |
| QQQ | +0.25% | 739.77 |
| IWM | −0.40% | 277.89 |
| NVDA | +0.51% | 228.38 |
| TSLA | +0.56% | 354.81 |
| AAPL | +1.10% | 333.02 |
| MSFT | +0.77% | 512.90 |
| AMZN | +1.01% | 249.15 |
| META | −1.84% | 725.18 |
| GOOGL | +0.93% | 344.08 |
| AMD | +0.69% | 611.76 |
| NFLX | −1.02% | 69.58 |
| COIN | −1.90% | 186.41 |
| PLTR | +0.04% | 187.05 |
| MSTR | −1.02% | 153.09 |
| SMCI | +0.12% | 41.07 |
| CRWD | +0.77% | 264.75 |
| ORCL | · | — |
| UBER | −1.23% | 68.51 |
| PYPL | −2.52% | 52.53 |
| MARA | −5.50% | 11.33 |
| RIOT | −5.80% | 20.15 |
| HOOD | −3.20% | 112.50 |
| SOFI | −1.19% | 15.72 |
| BAC | −0.96% | 54.43 |
| INTC | +3.71% | 120.23 |
| DIS | −0.48% | 104.90 |
| SNAP | +1.12% | 5.40 |
| LYFT | −0.40% | 15.01 |
| TGT | +0.17% | 156.69 |
| NKE | −1.23% | 35.40 |
| COF | −1.73% | 193.07 |

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