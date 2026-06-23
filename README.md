# Phantom Traders — site

Static site for **aiphantomtraders.com**, served by Cloudflare Pages from the
repo root. No Cloudflare build step — the **served `index.html` at the repo root
is a build artifact** produced from `src/index.html`.

## Editing the site

1. Edit **`src/index.html`** (the readable source of truth) — never edit root `index.html` directly.
2. Run the build: `npm install` then `npm run build`.
   - This minifies inline CSS (clean-css) + inline JS (terser, `mangle:false` so the
     global functions used by inline `onclick=` handlers are never renamed) and writes
     the optimized result to root `index.html`.
3. Commit **both** `src/index.html` and the regenerated root `index.html`.

> If you edit root `index.html` by hand, the next build will overwrite it. Always edit `src/`.

## Data

- Homepage ticker reads real quotes from the Supabase `home_quotes` view (over `market_cache`).
- Auth / signup / referrals go through the Render backend (`phantom-traders-backend.onrender.com`),
  kept warm by `.github/workflows/keepalive.yml`.

## Audits

`.github/workflows/site-audit.yml` renders every page with real Chrome (Playwright),
detects source-code leaks, runs a feature click-test, scrapes the live ticker, and runs
Lighthouse. Results are committed to `audit-results/`. On `main` it audits the live site;
on `claude/**` branches it serves and audits the branch build.
