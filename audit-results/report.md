# Live audit + feature test — http://localhost:8080

2026-06-23T15:37:15.024Z → 2026-06-23T15:39:29.341Z

## Findings

- **HIGH** — Homepage ticker grid only populated 0/32 symbols with real % — backend cold or symbol coverage gap.
- **HIGH** — No /market/quote response observed — backend likely cold (Render free tier).

## Source-code leak (visible raw code on page)

_No raw source detected in visible text._

## Feature click-test errors

- `home` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `home` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `features` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `features` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `pricing` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `pricing` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `products` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `products` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `blog` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `blog` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `discord` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `discord` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `dashboard` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `dashboard` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `signup` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `signup` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `legal` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `legal` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `docs` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `docs` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `store` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.
- `store` [onclick]: TimeoutError: elementHandle.click: Timeout 1500ms exceeded.


## Live ticker (homepage grid + tape)

Clock `MARKET · 15:37:25 ET`

| Symbol | Grid % | Tape px |
|---|---:|---:|
| SPY | · | — |
| QQQ | · | — |
| IWM | · | — |
| NVDA | · | — |
| TSLA | · | — |
| AAPL | · | — |
| MSFT | · | — |
| AMZN | · | — |
| META | · | — |
| GOOGL | · | — |
| AMD | · | — |
| NFLX | · | — |
| COIN | · | — |
| PLTR | · | — |
| MSTR | · | — |
| SMCI | · | — |
| CRWD | · | — |
| ORCL | · | — |
| UBER | · | — |
| PYPL | · | — |
| MARA | · | — |
| RIOT | · | — |
| HOOD | · | — |
| SOFI | · | — |
| BAC | · | — |
| INTC | · | — |
| DIS | · | — |
| SNAP | · | — |
| LYFT | · | — |
| TGT | · | — |
| NKE | · | — |
| COF | · | — |

## Market API

_no /market/quote call observed_

## Pages

| Page | Viewport | HTTP | OK | Console errs |
|---|---|---|---|---|
| home | desktop | 200 | ✅ | 4 |
| home | mobile | 200 | ✅ | 4 |
| features | desktop | 200 | ✅ | 4 |
| features | mobile | 200 | ✅ | 4 |
| pricing | desktop | 200 | ✅ | 4 |
| pricing | mobile | 200 | ✅ | 4 |
| products | desktop | 200 | ✅ | 4 |
| products | mobile | 200 | ✅ | 4 |
| blog | desktop | 200 | ✅ | 4 |
| blog | mobile | 200 | ✅ | 4 |
| discord | desktop | 200 | ✅ | 4 |
| discord | mobile | 200 | ✅ | 4 |
| dashboard | desktop | 200 | ✅ | 4 |
| dashboard | mobile | 200 | ✅ | 4 |
| signup | desktop | 200 | ✅ | 4 |
| signup | mobile | 200 | ✅ | 4 |
| legal | desktop | 200 | ✅ | 4 |
| legal | mobile | 200 | ✅ | 0 |
| docs | desktop | 200 | ✅ | 4 |
| docs | mobile | 200 | ✅ | 0 |
| store | desktop | 200 | ✅ | 4 |
| store | mobile | 200 | ✅ | 4 |