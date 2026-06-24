# Phantom Traders — Live Site Audit

**Site:** https://aiphantomtraders.com (Cloudflare Pages SPA → `/api/*` proxy → `phantom-traders-backend.onrender.com`; auth/data on Supabase `gzdhauxqrfbhbrfcscna`)
**Date:** 2026-06-05
**Branch:** `claude/pt-website-audit-playwright-iAQxp`

## Method & honest caveat

The original ask was Playwright + Firecrawl to render every page live. Two hard
constraints in this environment changed the approach:

1. **Playwright MCP and Firecrawl MCP are not connected to this session.** The
   repo's CLAUDE.md lists Playwright, but it isn't wired into this run.
2. **The egress network policy blocks the live host.** Both
   `aiphantomtraders.com` and the Render backend return `403 Host not in
   allowlist` from the sandbox proxy (not Cloudflare) — so no in-sandbox tool can
   fetch the rendered page.

So I could **not** pixel-render pages, check mobile breakpoints, or run
Lighthouse. Instead I audited the two things that actually matter for "is it
showing up-to-date real-time data" from authoritative sources I *can* reach:
the **source HTML** (full `index.html`), the **Supabase data layer** (the real
store), **TradingView MCP** (ground-truth prices), and **Sentry** (live errors).
Net result is arguably stronger on the data-freshness question, weaker on visual
QA. To finish the visual/Lighthouse half, connect Playwright/Firecrawl or
allowlist the domain (see "To complete the audit").

---

## Verdict

The **backend data pipeline is healthy and genuinely real-time** — but the
**website can display 18-month-old prices under a "LIVE" badge**, ships
**proprietary trading data to the public**, and advertises **fabricated
reviews**. Not launch-ready until the three criticals below are fixed.

---

## CRITICAL 1 — Frontend shows stale 2024 prices labeled "LIVE"

`index.html` hardcodes a fallback price table (`tickerData`, ~line 1957) that is
~18 months out of date. It renders immediately on load and is only overwritten
*if* the Render backend answers within a **6-second timeout** (`fetchTickerPrices`,
line 2020-2040). Render's free tier sleeps after 15 min idle, so the first
visitor in any idle window sees the stale table — while the nav shows
`MARKET · LIVE` and the badge flips to `● LIVE`.

Hardcoded fallback vs. **actual current price** (TradingView + Supabase
`market_cache`, both pulled today 06:3x UTC and in agreement to the cent):

| Symbol | Site fallback | Real (today) | Off by |
|--------|--------------:|-------------:|-------:|
| AAPL   | $213.49 | $311.23 | **−31%** |
| NVDA   | $121.44 | $218.66 | **−44%** |
| GOOGL  | $172.63 | $372.19 | **−54%** |
| TSLA   | $248.71 | $418.45 | **−41%** |
| AMD    | $156.22 | $523.20 | **−70%** |
| INTC   |  $22.84 | $111.78 | **−80%** |
| AMZN   | $208.84 | $253.79 | −18% |
| MSFT   | $415.32 | $428.05 | −3% |
| META   | $612.18 | $627.57 | −2% |

The data *source* is fine — `market_cache` for AAPL/NVDA/TSLA/AMD/INTC/GOOGL/SPY
was updated **today at 06:32 UTC** and matches TradingView exactly. This is a
**frontend-only defect**: a stale literal + a fragile single source (cold Render).

**Fix (recommended):** drop the hardcoded prices and read the fallback straight
from Supabase `market_cache` — the anon Supabase client is already loaded on the
page (line 516-517), so the ticker can hydrate from the DB even when Render is
cold. At minimum: do not render literal prices and do not show the LIVE badge
until a real fetch succeeds (show a skeleton/`—`). Optionally add a keep-alive
ping to the Render service.

## CRITICAL 2 — 26 Supabase tables have RLS disabled, exposed to the public anon key

The anon key ships in the page (`index.html:517`). That is normal for Supabase
**only when every table has Row-Level Security**. 26 do not, so anyone with the
key (i.e. anyone) can **read and write** them. Highlights:

- **Proprietary IP leak (read):** `options_flow` (28,608 rows), `insider_filings`
  (913), `gex_snapshot` (819), `short_interest`, `search_trends`,
  `macro_features`, and the `_disc_spy_*` strategy-feature tables (43k+ rows).
- **Risk-control tampering (write):** `protective_mode` (the drawdown **kill
  switch** state), `disabled_strategies`, `strategy_tiers`, `tod_score_weights`.
  An attacker could clear the kill switch or disable strategies.

The frontend never reads these tables (only user-facing ones, which *are* RLS'd),
so the right fix is **RLS on + no policies = service-role-only**. Supabase's
advisor flagged this; remediation SQL is in `migrations/` proposal below. **Do
not run blindly** — enabling RLS without policies blocks all anon/auth access by
design; that's correct *here* because these are backend-only tables. Verify no
client path reads them first.

```sql
-- Backend-only tables → service-role only. Review before running.
ALTER TABLE public.options_flow            ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.insider_filings         ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.gex_snapshot            ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.short_interest          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.search_trends           ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.macro_features          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.macro_events            ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.protective_mode         ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.disabled_strategies     ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.strategy_tiers          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tod_score_weights       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.strategy_exit_profiles  ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.options_chain_history   ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.underlying_bars         ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.iv_history              ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.trade_assertions        ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tv_webhook_log          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.entry_skip_log          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.market_features_cache   ENABLE ROW LEVEL SECURITY;
ALTER TABLE public._disc_spy_sqqq_d_feat   ENABLE ROW LEVEL SECURITY;
ALTER TABLE public._disc_spy_5m_feat       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public._disc_spy_15m_feat      ENABLE ROW LEVEL SECURITY;
ALTER TABLE public._disc_spy_1h_feat       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.active_strategies_backup_2026_05_26          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.strategy_exit_profiles_backup_2026_05_26     ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.bot_paper_trades_pre_2026_05_26             ENABLE ROW LEVEL SECURITY;
```

## CRITICAL 3 — Fabricated reviews / ratings

JSON-LD ships `aggregateRating` **4.8 / 312 reviews** (`index.html:67-71`) while
the `testimonials` table is **empty** and there are **2 real user profiles / 2
email captures**. Also hardcoded: `★4.8 (198 reviews)` (line 1497) and course
cards with `reviews:312/248/189/156` (lines 4059+).

This is a Google review-snippet **policy violation** (risk of manual action) and
a trust/regulatory risk for a finance product. **Remove `aggregateRating` from
JSON-LD** and gate displayed review counts until real reviews exist.

---

## Medium / Low

- **Single point of failure for market data:** everything routes through one
  Render free-tier service. Supabase `market_cache` already holds the same fresh
  quotes with better availability — prefer it (ties into Critical 1).
- **Brand inconsistency:** `<title>` = "Institutional-Grade Portfolio
  Intelligence" vs OG/Twitter = "Trade Smarter. Not Harder." Pick one.
- **Demo data** (sample portfolios, lines ~2897-2975) is hardcoded — fine, but
  confirm it's clearly labeled "sample" so it isn't read as live performance.
- **Visual / responsive / Lighthouse not verified** — needs a real browser
  (see below).

## Healthy / passing

- **Real-time pipeline is live:** latest `bot_heartbeats` 06:34 UTC today; 2
  bots (Phantom + Bullseye) active in 24h; `market_cache` fresh and accurate.
- **Sentry** wired (`index.html:6`), **0 unresolved errors in 30 days.**
- **Security headers** present (`_headers`): HSTS preload, CSP, X-Frame DENY,
  nosniff. CSP `connect-src` correctly scoped to Supabase + backend.
- Recent **XSS hardening** (DOMPurify on blog, escaped admin interpolation).
- **RLS is correctly ON** for all user-facing tables (profiles, portfolios,
  holdings, trades, alerts, watchlist, course_purchases).
- SEO basics solid: canonical, OG/Twitter, sitemap, robots, manifest, SW, JSON-LD
  (minus the fake rating).

---

## To complete the audit (visual half)

Requires a real browser the live host will serve:
1. Connect Playwright MCP or Firecrawl MCP to the session, **or** add
   `aiphantomtraders.com` + `phantom-traders-backend.onrender.com` to the
   environment's egress allowlist; then
2. Render each page (`#page-features`, `#pricing`, `#products`, `#blog`,
   `#discord`, `#dashboard`, `#signup`, `#legal`), capture the live ticker
   values, walk the signup/checkout flow, and run Lighthouse (perf/a11y/SEO) at
   desktop + 375/768px.

## Suggested next actions (need your go-ahead)

- [x] Patch Critical 1 — ticker reads Supabase `home_quotes` view (fresh prices, no 2024 fallback literals)
- [x] Apply Critical 2 RLS migration (2026-06-23) — confirmed zero of the 26 backend tables are
  read by any client path (frontend only touches user-facing RLS'd tables); enabled RLS (no
  policies = service-role-only) on all 26 via Supabase SQL Editor. Verification query returns zero
  RLS-disabled public tables. Migration committed to `phantom-traders-backend`
  (`rls_lockdown_backend_tables.sql`).
- [x] Patch Critical 3 (2026-06-23) — `aggregateRating` removed from JSON-LD; fabricated
  storefront stats (`312+ Students`, `4.8★ Avg Rating`, `Students enrolled`) replaced with
  factual product counts (9 courses / 5 mastery guides / lifetime access); dead testimonials
  carousel (invented names/quotes) deleted; unused per-item `rating`/`reviews` data fields
  stripped. Real reviews still flow via the user submission form → `testimonials` table → admin tab.

---

## Static SEO / A11y / Perf pass (2026-06-24)

The live-render half of the audit (Lighthouse, mobile breakpoints, walking the
signup/checkout flow) still requires a browser the host will serve — egress to
`aiphantomtraders.com` + the Render backend is **still blocked** by the
environment network policy (proxy returns 403 on CONNECT), and no Playwright /
Firecrawl / Chrome-DevTools MCP is connected. To finish it: allowlist those two
domains in the environment's network policy, or connect a browser MCP. Below is
everything checkable from source.

### SEO — strong
- `<title>` 43 chars ✅, brand now consistent across title/OG/Twitter/JS PAGE_TITLES.
- canonical, viewport, `lang="en"`, robots, sitemap, 7+ OG tags, Twitter card, JSON-LD all present ✅
- **Minor:** `meta description` is 201 chars — Google truncates ~155–160; keywords are front-loaded so impact is low. Left as-is (trimming would drop the "Start free" CTA).
- **Minor/by-design:** 36 `<h1>` elements across the SPA's hidden page-sections — only one is visible at a time, but crawlers see all. Acceptable for this SPA pattern; revisit if SEO ranking suffers.

### Accessibility — good, one fix applied
- 21 images, **0 missing alt** ✅; 74 inputs / 76 `<label>` ✅ strong form labeling.
- **Fixed (2026-06-24):** 9 icon-only buttons (password toggle, remove-ticker, set-alert, delete-alert, journal prev/next, close, delete-live-alert) had no accessible name → added `aria-label` to each.
- **Note:** no ARIA landmark `role=`s; relies on native semantics. Adding `role="navigation"/"main"` would help screen-reader navigation — deferred (needs live SR testing to validate).

### Performance — needs live Lighthouse; static signals
- Single self-contained HTML (~774 KB built, inline CSS+JS, no framework, no render-blocking external CSS bundle). One request vs. no code-splitting — borderline for LCP on a marketing page; confirm with Lighthouse.
- `preload: 0` — preloading the hero font/critical asset could improve LCP.
- Only 2 of 21 images use `loading="lazy"` — add to below-the-fold images.
- Keep-alive ping warms the cold Render free tier (mitigates auth/checkout cold start).

### Responsive — excellent
- **31 max-width breakpoints** (120 → 1400px) plus min-width queries. Comprehensive coverage; no static red flags. Still worth a real-device pass at 375/768px once a browser is available.
