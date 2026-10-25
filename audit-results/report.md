# Live audit + feature test — https://aiphantomtraders.com

2026-10-25T20:58:51.551Z → 2026-10-25T21:01:15.193Z

## Findings

- **HIGH** — No /market/quote response observed — backend likely cold (Render free tier).

## Source-code leak (visible raw code on page)

_No raw source detected in visible text._

## Feature click-test errors

_No errors thrown while clicking tabs / dropdowns / FAQ / CTAs._


## Live ticker (homepage grid + tape)

Clock `MARKET · 20:59:01 ET`

| Symbol | Grid % | Tape px |
|---|---:|---:|
| SPY | −0.52% | 759.97 |
| QQQ | −0.01% | 704.40 |
| IWM | −0.33% | 275.75 |
| NVDA | −0.59% | 210.96 |
| TSLA | −0.63% | 372.22 |
| AAPL | −0.14% | 347.73 |
| MSFT | +0.66% | 524.51 |
| AMZN | −0.95% | 248.00 |
| META | −0.96% | 642.62 |
| GOOGL | −1.24% | 320.21 |
| AMD | +1.74% | 516.79 |
| NFLX | −1.79% | 65.85 |
| COIN | −2.74% | 164.45 |
| PLTR | +0.29% | 196.75 |
| MSTR | +0.14% | 146.01 |
| SMCI | −2.31% | 32.94 |
| CRWD | +8.25% | 257.57 |
| ORCL | · | — |
| UBER | −3.43% | 66.70 |
| PYPL | −0.90% | 57.02 |
| MARA | −3.17% | 7.02 |
| RIOT | −2.79% | 12.53 |
| HOOD | −1.56% | 95.07 |
| SOFI | −1.05% | 14.62 |
| BAC | −1.02% | 50.56 |
| INTC | +1.72% | 86.96 |
| DIS | −0.54% | 112.52 |
| SNAP | −0.16% | 6.34 |
| LYFT | −2.81% | 16.94 |
| TGT | −3.38% | 152.76 |
| NKE | −2.66% | 37.30 |
| COF | −1.03% | 201.34 |

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
| blog | desktop | — | ❌ | 0 |
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