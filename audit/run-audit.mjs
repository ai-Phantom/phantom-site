// Live audit harness for https://aiphantomtraders.com
// Runs in CI (GitHub Actions) where egress is open and a real Chromium exists.
// - Renders every page at desktop (1440) and mobile (375)
// - Screenshots each, collects console errors / failed requests
// - Scrapes the live ticker + /market/quote response to test the stale-data bug
// Outputs: audit/out/{report.json, report.md, *.png}
import { chromium, devices } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';

const BASE = process.env.AUDIT_BASE_URL || 'https://aiphantomtraders.com';
const OUT = new URL('./out/', import.meta.url).pathname;

// Hash routes from sitemap.xml
const PAGES = [
  { id: 'home',      hash: '' },
  { id: 'features',  hash: '#page-features' },
  { id: 'pricing',   hash: '#page-pricing' },
  { id: 'products',  hash: '#page-products' },
  { id: 'blog',      hash: '#page-blog' },
  { id: 'discord',   hash: '#page-discord' },
  { id: 'dashboard', hash: '#page-dashboard' },
  { id: 'signup',    hash: '#page-signup' },
  { id: 'legal',     hash: '#page-legal' },
];

// Known hardcoded fallback prices in index.html (~2024). If the live ticker
// still shows these, the cold-backend fallback is on screen under a LIVE badge.
const STALE_FALLBACK = { AAPL: 213.49, NVDA: 121.44, AMD: 156.22, INTC: 22.84, TSLA: 248.71, GOOGL: 172.63 };

const report = { base: BASE, startedAt: new Date().toISOString(), pages: [], ticker: null, marketApi: null, findings: [] };

async function auditPage(browser, viewport, page) {
  const ctx = await browser.newContext(
    viewport === 'mobile' ? { ...devices['iPhone 13'] } : { viewport: { width: 1440, height: 900 } }
  );
  const pg = await ctx.newPage();
  const consoleErrors = [], failedRequests = [];
  pg.on('console', (m) => { if (m.type() === 'error') consoleErrors.push(m.text().slice(0, 300)); });
  pg.on('pageerror', (e) => consoleErrors.push('pageerror: ' + String(e).slice(0, 300)));
  pg.on('requestfailed', (r) => failedRequests.push(`${r.failure()?.errorText || 'fail'} ${r.url().slice(0, 160)}`));

  // Capture the live market quote response (only matters on home)
  if (page.id === 'home') {
    pg.on('response', async (resp) => {
      if (resp.url().includes('/market/quote')) {
        try { report.marketApi = { url: resp.url(), status: resp.status(), body: (await resp.text()).slice(0, 800) }; }
        catch { report.marketApi = { url: resp.url(), status: resp.status(), body: '<unreadable>' }; }
      }
    });
  }

  const entry = { id: page.id, viewport, url: BASE + '/' + page.hash, ok: false };
  try {
    const resp = await pg.goto(BASE + '/' + page.hash, { waitUntil: 'networkidle', timeout: 45000 });
    entry.httpStatus = resp?.status();
    entry.title = await pg.title();
    await pg.waitForTimeout(page.id === 'home' ? 9000 : 1500); // let ticker fetch resolve on home

    if (page.id === 'home' && viewport === 'desktop') {
      const ticker = await pg.evaluate(() => {
        const out = {};
        document.querySelectorAll('#tickerTrack [data-ticker]').forEach((el) => {
          const sym = el.getAttribute('data-ticker');
          const price = el.querySelector('.tk-price')?.textContent?.replace(/[^0-9.]/g, '');
          if (sym && price && !(sym in out)) out[sym] = parseFloat(price);
        });
        const badge = document.getElementById('tickerLiveBadge')?.textContent?.trim() || null;
        const clock = document.getElementById('navLiveClock')?.textContent?.trim() || null;
        return { prices: out, badge, clock };
      });
      report.ticker = ticker;
      const stale = Object.entries(STALE_FALLBACK).filter(
        ([s, v]) => ticker.prices[s] != null && Math.abs(ticker.prices[s] - v) < 1.0
      ).map(([s]) => s);
      if (stale.length) {
        report.findings.push({
          severity: 'CRITICAL',
          finding: `Live ticker is showing hardcoded 2024 fallback prices for: ${stale.join(', ')} ` +
                   `while badge reads "${ticker.badge}". Backend quote was not applied before render.`,
        });
      }
    }

    const shot = `${OUT}${page.id}-${viewport}.png`;
    await pg.screenshot({ path: shot, fullPage: true });
    entry.screenshot = shot.split('/').pop();
    entry.ok = true;
  } catch (e) {
    entry.error = String(e).slice(0, 300);
  }
  entry.consoleErrors = consoleErrors;
  entry.failedRequests = failedRequests;
  report.pages.push(entry);
  await ctx.close();
}

// Prefer real Google Chrome (channel: 'chrome'); fall back to bundled Chromium.
let browser;
try { browser = await chromium.launch({ channel: 'chrome' }); }
catch { browser = await chromium.launch(); }
await mkdir(OUT, { recursive: true });
for (const p of PAGES) { await auditPage(browser, 'desktop', p); await auditPage(browser, 'mobile', p); }
await browser.close();

// market api health finding
if (!report.marketApi) {
  report.findings.push({ severity: 'HIGH', finding: 'No /market/quote response observed within page load window — backend likely cold (Render free tier sleeps after 15 min idle).' });
} else if (report.marketApi.status !== 200) {
  report.findings.push({ severity: 'HIGH', finding: `/market/quote returned HTTP ${report.marketApi.status}.` });
}

report.finishedAt = new Date().toISOString();
await writeFile(`${OUT}report.json`, JSON.stringify(report, null, 2));

const md = [];
md.push(`# Live render audit — ${BASE}`, '', `Run: ${report.startedAt} → ${report.finishedAt}`, '');
md.push('## Findings', '');
md.push(report.findings.length ? report.findings.map(f => `- **${f.severity}** — ${f.finding}`).join('\n') : '- None flagged by automated checks.');
md.push('', '## Live ticker', '');
if (report.ticker) {
  md.push(`Badge: \`${report.ticker.badge}\` · Clock: \`${report.ticker.clock}\``, '');
  md.push('| Symbol | Displayed |', '|---|---:|', ...Object.entries(report.ticker.prices).map(([s, v]) => `| ${s} | ${v} |`));
} else md.push('_Ticker not captured._');
md.push('', '## Market API', '', report.marketApi ? `\`${report.marketApi.status}\` ${report.marketApi.url}` : '_No /market/quote call observed (cold backend?)._');
md.push('', '## Pages', '', '| Page | Viewport | HTTP | OK | Console errs | Failed reqs |', '|---|---|---|---|---|---|');
for (const p of report.pages) md.push(`| ${p.id} | ${p.viewport} | ${p.httpStatus ?? '—'} | ${p.ok ? '✅' : '❌'} | ${p.consoleErrors.length} | ${p.failedRequests.length} |`);
await writeFile(`${OUT}report.md`, md.join('\n'));

console.log(md.join('\n'));
console.log(`\nFindings: ${report.findings.length}. Screenshots + JSON in audit/out/.`);
