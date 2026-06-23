# Live audit + feature test — https://aiphantomtraders.com

2026-06-23T19:58:47.303Z → 2026-06-23T20:02:35.813Z

## Findings

- **HIGH** — No /market/quote response observed — backend likely cold (Render free tier).

## Source-code leak (visible raw code on page)

_No raw source detected in visible text._

## Feature click-test errors

_No errors thrown while clicking tabs / dropdowns / FAQ / CTAs._


## Live ticker (homepage grid + tape)

Clock `MARKET · 19:58:57 ET`

| Symbol | Grid % | Tape px |
|---|---:|---:|
| SPY | −1.27% | 734.97 |
| QQQ | −3.12% | 714.93 |
| IWM | −0.79% | 295.81 |
| NVDA | −3.95% | 200.41 |
| TSLA | −5.78% | 381.64 |
| AAPL | −0.19% | 296.46 |
| MSFT | +2.11% | 375.09 |
| AMZN | +0.85% | 234.78 |
| META | −0.23% | 562.57 |
| GOOGL | −0.72% | 347.16 |
| AMD | −5.88% | 519.18 |
| NFLX | +0.03% | 72.90 |
| COIN | −3.95% | 158.33 |
| PLTR | −2.31% | 116.74 |
| MSTR | −4.60% | 104.43 |
| SMCI | −5.87% | 33.38 |
| CRWD | +0.85% | 681.20 |
| ORCL | −3.18% | 172.14 |
| UBER | −0.03% | 77.47 |
| PYPL | −1.23% | 41.82 |
| MARA | −0.81% | 14.73 |
| RIOT | +0.03% | 28.64 |
| HOOD | −2.44% | 103.13 |
| SOFI | +1.11% | 17.29 |
| BAC | +1.06% | 57.98 |
| INTC | −6.18% | 132.23 |
| DIS | +1.27% | 103.75 |
| SNAP | −3.46% | 4.47 |
| LYFT | −2.67% | 13.84 |
| TGT | +3.41% | 134.16 |
| NKE | −1.57% | 42.51 |
| COF | −1.51% | 197.67 |

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
| products | desktop | 200 | ✅ | 5 |
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