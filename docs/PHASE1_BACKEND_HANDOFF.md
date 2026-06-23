# Phase 1 — Backend handoff (`Phantom-traders-backend`)

Context brief for a Claude Code session scoped to **`ai-Phantom/Phantom-traders-backend`**.
Written from the `phantom-site` session that shipped Phases 0–3 of the marketing site.

## What this backend is
- Python service, deployed on **Render** at `phantom-traders-backend.onrender.com`
  (auto-deploys on push to `main` — you never touch the Render dashboard).
- Backend for the live site **`aiphantomtraders.com`** (repo `phantom-site`).
- Serves at least: `/market/quote`, `/auth/signup`, `/auth/me`, `/referrals/*`.

## The core problem
`GET /market/quote?symbols=SPY,QQQ,...` **returns an empty array `[]`** (HTTP 200, no data).
Confirmed via live audit. Because of this, the site's homepage ticker had to be
**re-routed to a Supabase view** as a workaround instead of using this endpoint.

## Data layer (Supabase project `gzdhauxqrfbhbrfcscna`)
- `market_cache` — columns incl. `ticker, price, prev_close, day_high, day_low,
  day_open, volume, updated_at, rsi, macd, ...`. The bots keep most mega-caps fresh
  (updated_at ~now); a few symbols (ORCL, UBER, QCOM, CRM) drift stale (days/months old).
- `home_quotes` — a curated **public read-only view** created over `market_cache`
  during the site work, exposing only `ticker, price, prev_close, day_chg_pct, updated_at`.
  The site reads this with the anon key. (Most `market_cache`-adjacent tables had RLS
  enabled/locked in the site work — service-role still bypasses.)

## Phase 1 tasks (priority order)
1. **Fix `/market/quote` returning `[]`.** Find the data source (Finnhub key? reads
   `market_cache`? something unconfigured on Render env?), reproduce the empty response,
   and make it return real quotes for the requested symbols. This is the top item.
2. **Cold-start hardening.** Render free tier sleeps after ~15 min. Ensure a real
   `/health` endpoint; decide keep-alive vs. paid tier. (A GitHub Action in `phantom-site`
   — `.github/workflows/keepalive.yml` — already pings this backend every ~10 min.)
3. **Market-scan cadence.** Make sure the symbols the homepage ticker shows stay fresh
   (don't let ORCL/UBER/QCOM/CRM drift). Either widen the scan set or add a refresh job.

## Site-side context you may want
- Homepage ticker symbols (curated to what the backend/cache covers):
  SPY, QQQ, IWM, NVDA, TSLA, AAPL, MSFT, AMZN, META, GOOGL, AMD, NFLX, COIN, PLTR,
  MSTR, SMCI, CRWD, ORCL, UBER, PYPL, MARA, RIOT, HOOD, SOFI, BAC, INTC, DIS, SNAP,
  LYFT, TGT, NKE, COF.
- Once `/market/quote` works, the site could optionally switch its ticker back to the
  backend, but the Supabase `home_quotes` path is fine and resilient — coordinate before
  changing the site.

## How to verify
1. Read repo structure + the market route; reproduce the `[]` response locally or against
   the deployed URL.
2. Fix, push to `main` → Render auto-deploys.
3. Verify the live endpoint returns real data:
   `curl "https://phantom-traders-backend.onrender.com/market/quote?symbols=SPY,NVDA"`.

## Tooling available in a typical session
GitHub, Supabase (project `gzdhauxqrfbhbrfcscna`), TradingView, Sentry, PostHog MCPs —
use TradingView/Supabase to sanity-check quote values.
