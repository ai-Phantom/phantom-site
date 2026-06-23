// Live audit + feature test for https://aiphantomtraders.com
// Runs in CI (open egress, real Chrome). Writes:
//   audit/out/*            -> screenshots + report (uploaded as artifact)
//   audit-results/report.* -> committed back to the branch so Claude can read it
//
// Checks:
//   1. SOURCE-CODE LEAK: visible text (excluding intended <pre>/<code> samples)
//      that contains HTML tags or JS syntax = raw source rendering on the page.
//   2. FEATURE TEST: clicks every nav link, tab, dropdown, FAQ, accordion, CTA
//      and records any thrown error or console error.
//   3. DATA FRESHNESS: scrapes the live ticker + /market/quote response.
import { chromium, devices } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';

const BASE = process.env.AUDIT_BASE_URL || 'https://aiphantomtraders.com';
const ART = new URL('./out/', import.meta.url).pathname;           // audit/out
const REPO = new URL('../audit-results/', import.meta.url).pathname; // repo-root/audit-results

const PAGES = [
  { id: 'home', hash: '' }, { id: 'features', hash: '#page-features' },
  { id: 'pricing', hash: '#page-pricing' }, { id: 'products', hash: '#page-products' },
  { id: 'blog', hash: '#page-blog' }, { id: 'discord', hash: '#page-discord' },
  { id: 'dashboard', hash: '#page-dashboard' }, { id: 'signup', hash: '#page-signup' },
  { id: 'legal', hash: '#page-legal' }, { id: 'docs', hash: '#page-docs' },
  { id: 'store', hash: '#page-store' },
];
const STALE_FALLBACK = { AAPL: 213.49, NVDA: 121.44, AMD: 156.22, INTC: 22.84, TSLA: 248.71, GOOGL: 172.63 };

const report = { base: BASE, startedAt: new Date().toISOString(), pages: [], leaks: [], ticker: null, marketApi: null, featureErrors: [], findings: [] };

// Returns visible text with intended code samples removed, so any HTML/JS
// syntax left over is genuinely leaking into the page.
const SCAN = () => {
  const clone = document.body.cloneNode(true);
  clone.querySelectorAll('script,style,pre,code,.doc-code-block,.doc-code,template,noscript').forEach((n) => n.remove());
  return clone.innerText || '';
};
const LEAK_RX = [
  /<\/?(div|span|script|style|a|button|svg|p|h[1-6])\b[^>]*>/i, // literal HTML tags as text
  /\bfunction\s*\(/, /=>\s*[{(]/, /\bdocument\.(getElementById|querySelector)/,
  /addEventListener\(/, /\bconst\s+\w+\s*=/, /style="[^"]*"/, /class="[^"]*"/,
];
function findLeaks(text) {
  const hits = [];
  for (const line of text.split('\n')) {
    const t = line.trim();
    if (t.length < 8) continue;
    if (LEAK_RX.some((rx) => rx.test(t))) hits.push(t.slice(0, 220));
  }
  return [...new Set(hits)].slice(0, 25);
}

async function exerciseFeatures(pg, pageId) {
  // Click-test every interactive surface; record errors. Bounded per selector.
  const selectors = [
    '.feat-tab', '.demo-tab', '.prod-tab', '.legal-tab', '.store-page-tab', '.blog-cat-btn',
    '.faq-q', '.legal-accordion-header', '.nav-drop-item', '.store-filter-btn',
    'a[href^="#page-"]', '[onclick]',
  ];
  for (const sel of selectors) {
    const els = await pg.$$(sel);
    for (const el of els.slice(0, 12)) {
      try {
        if (await el.isVisible()) { await el.click({ timeout: 1500, trial: false }); await pg.waitForTimeout(120); }
      } catch (e) {
        report.featureErrors.push({ page: pageId, selector: sel, error: String(e).split('\n')[0].slice(0, 160) });
      }
    }
  }
}

async function auditPage(browser, viewport, page, exercise) {
  const ctx = await browser.newContext(viewport === 'mobile' ? { ...devices['iPhone 13'] } : { viewport: { width: 1440, height: 900 } });
  const pg = await ctx.newPage();
  const consoleErrors = [];
  pg.on('console', (m) => { if (m.type() === 'error') consoleErrors.push(m.text().slice(0, 200)); });
  pg.on('pageerror', (e) => consoleErrors.push('pageerror: ' + String(e).slice(0, 200)));
  if (page.id === 'home') pg.on('response', async (r) => {
    if (r.url().includes('/market/quote')) { try { report.marketApi = { status: r.status(), body: (await r.text()).slice(0, 600) }; } catch { report.marketApi = { status: r.status() }; } }
  });

  const entry = { id: page.id, viewport, url: BASE + '/' + page.hash, ok: false };
  try {
    const resp = await pg.goto(BASE + '/' + page.hash, { waitUntil: 'load', timeout: 30000 });
    entry.httpStatus = resp?.status();
    await pg.waitForTimeout(page.id === 'home' ? 9000 : 1500);

    // SOURCE-CODE LEAK scan
    const cleaned = await pg.evaluate(SCAN);
    const leaks = findLeaks(cleaned);
    if (leaks.length) report.leaks.push({ page: page.id, viewport, samples: leaks });

    // ticker scrape on home/desktop
    if (page.id === 'home' && viewport === 'desktop') {
      report.ticker = await pg.evaluate(() => {
        const out = {};
        document.querySelectorAll('#tickerTrack [data-ticker]').forEach((el) => {
          const s = el.getAttribute('data-ticker'); const p = el.querySelector('.tk-price')?.textContent?.replace(/[^0-9.]/g, '');
          if (s && p && !(s in out)) out[s] = parseFloat(p);
        });
        return { prices: out, badge: document.getElementById('tickerLiveBadge')?.textContent?.trim() || null, clock: document.getElementById('navLiveClock')?.textContent?.trim() || null };
      });
      const stale = Object.entries(STALE_FALLBACK).filter(([s, v]) => report.ticker.prices[s] != null && Math.abs(report.ticker.prices[s] - v) < 1).map(([s]) => s);
      if (stale.length) report.findings.push({ severity: 'CRITICAL', finding: `Ticker shows hardcoded 2024 fallback for ${stale.join(', ')} under badge "${report.ticker.badge}".` });
    }

    if (exercise) await exerciseFeatures(pg, page.id);

    await pg.screenshot({ path: `${ART}${page.id}-${viewport}.png`, fullPage: true });
    entry.ok = true;
  } catch (e) { entry.error = String(e).slice(0, 200); }
  entry.consoleErrors = consoleErrors;
  report.pages.push(entry);
  await ctx.close();
}

let browser;
try { browser = await chromium.launch({ channel: 'chrome' }); } catch { browser = await chromium.launch(); }
await mkdir(ART, { recursive: true }); await mkdir(REPO, { recursive: true });
for (const p of PAGES) { await auditPage(browser, 'desktop', p, true); await auditPage(browser, 'mobile', p, false); }
await browser.close();

if (report.leaks.length) report.findings.unshift({ severity: 'CRITICAL', finding: `Source code is visibly rendering on ${report.leaks.length} page/viewport(s): ${[...new Set(report.leaks.map((l) => l.page))].join(', ')}.` });
if (!report.marketApi) report.findings.push({ severity: 'HIGH', finding: 'No /market/quote response observed — backend likely cold (Render free tier).' });
report.finishedAt = new Date().toISOString();

const md = [];
md.push(`# Live audit + feature test — ${BASE}`, '', `${report.startedAt} → ${report.finishedAt}`, '');
md.push('## Findings', '', report.findings.length ? report.findings.map((f) => `- **${f.severity}** — ${f.finding}`).join('\n') : '- None flagged.', '');
md.push('## Source-code leak (visible raw code on page)', '');
if (report.leaks.length) for (const l of report.leaks) { md.push(`### ${l.page} (${l.viewport})`, '```', ...l.samples, '```', ''); }
else md.push('_No raw source detected in visible text._', '');
md.push('## Feature click-test errors', '', report.featureErrors.length ? report.featureErrors.map((e) => `- \`${e.page}\` ${e.selector}: ${e.error}`).join('\n') : '_No errors thrown while clicking tabs / dropdowns / FAQ / CTAs._', '');
md.push('', '## Live ticker', '');
if (report.ticker) { md.push(`Badge \`${report.ticker.badge}\` · Clock \`${report.ticker.clock}\``, '', '| Symbol | Shown |', '|---|---:|', ...Object.entries(report.ticker.prices).map(([s, v]) => `| ${s} | ${v} |`)); } else md.push('_not captured_');
md.push('', '## Market API', '', report.marketApi ? `\`${report.marketApi.status}\`` : '_no /market/quote call observed_', '');
md.push('## Pages', '', '| Page | Viewport | HTTP | OK | Console errs |', '|---|---|---|---|---|', ...report.pages.map((p) => `| ${p.id} | ${p.viewport} | ${p.httpStatus ?? '—'} | ${p.ok ? '✅' : '❌'} | ${p.consoleErrors.length} |`));
const mdStr = md.join('\n');

for (const dir of [ART, REPO]) { await writeFile(`${dir}report.md`, mdStr); await writeFile(`${dir}report.json`, JSON.stringify(report, null, 2)); }
console.log(mdStr);
console.log(`\nLeaks: ${report.leaks.length} · Feature errors: ${report.featureErrors.length} · Findings: ${report.findings.length}`);
