# Live site audit harness

Renders every page of the live site with **real Google Chrome**, screenshots
desktop + mobile, scrapes the live ticker to detect the stale-market-data bug,
collects console errors, and runs Lighthouse.

## Why it runs in CI, not in the Claude web sandbox

The Claude Code **web** environment uses a restrictive egress allow-list. In a
session there on 2026-06-05, these hosts returned `403 Host not in allowlist`:

- `aiphantomtraders.com` and `phantom-traders-backend.onrender.com` (the audit targets)
- the Playwright browser CDN (so a headless browser can't even be downloaded)
- `api.firecrawl.dev`

`registry.npmjs.org`, `pypi.org`, and `github.com` are allowed. So the audit
can't reach the live site from that sandbox. GitHub Actions runners have open
egress and a real browser, so the audit runs there instead.

## Run it

**CI (recommended):** Actions → **Live Site Audit** → *Run workflow*. Artifacts:
`render-audit` (screenshots + `report.md`/`report.json`) and the Lighthouse report.
Also runs weekly (Mon 14:00 UTC) as a market-data freshness canary.

**Locally / any machine with internet:**
```bash
cd audit
npm install
npx playwright install --with-deps chrome
npm run audit            # writes audit/out/{report.md,report.json,*.png}
AUDIT_BASE_URL=https://staging.example.com npm run audit   # override target
```

## To run the browser MCPs *inside* a Claude session instead

`.mcp.json` (repo root) registers the **playwright**, **chrome-devtools**, and
**firecrawl** MCP servers. They only work when the session can reach the targets,
which means either:

1. a **local** Claude Code session (no egress limits), or
2. a **web** environment whose network policy allows `aiphantomtraders.com`,
   `phantom-traders-backend.onrender.com`, the Playwright CDN, and (for Firecrawl)
   `api.firecrawl.dev`. Set that policy when creating/editing the environment —
   see https://code.claude.com/docs/en/claude-code-on-the-web

Firecrawl also needs `FIRECRAWL_API_KEY` set as an environment variable.
