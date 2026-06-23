# Live audit + feature test — https://aiphantomtraders.com

2026-06-23T15:42:44.478Z → 2026-06-23T15:45:01.780Z

## Findings

- **HIGH** — Homepage ticker grid only populated 0/32 symbols with real % — backend cold or symbol coverage gap.

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

Clock `MARKET · 15:42:54 ET`

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

`200`

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