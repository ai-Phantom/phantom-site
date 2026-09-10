/**
 * Root middleware. Runs before static assets are served, so it is also the
 * enforcement point for "what must never be public".
 *
 * Context: this site is deployed by Cloudflare Pages from the REPO ROOT (see
 * README) — there is no build output directory, so every tracked file is
 * otherwise a public static asset. That meant `/src/index.html` (the full
 * unminified source, with developer comments, admin markup and table names),
 * plus build tooling, docs and CI config, were all fetchable. The SPA rule in
 * `_redirects` does not shield them because real files win over redirects.
 *
 * Everything not matched below falls through to `next()` unchanged.
 */

// Paths that must never be served. Matched case-insensitively against the
// pathname. Keep this in sync with anything added to the repo root.
const DENY_PREFIXES = [
  '/src/',            // unminified source of truth
  '/docs/',           // internal handoff docs
  '/audit/',          // audit tooling
  '/audit-results/',  // CI audit output
  '/.github/',        // workflows
  '/node_modules/',
  '/.git/',
  '/scripts/',
  '/functions/',      // this middleware's own source
];

// Dotfiles leak repo layout (.gitignore) or secrets (.env). `.well-known` is a
// real, spec'd public path (ACME / domain verification) and must stay reachable.
function isHiddenPath(pathname) {
  if (pathname.toLowerCase().startsWith('/.well-known/')) return false;
  return pathname.split('/').some((seg) => seg.startsWith('.') && seg.length > 1);
}

const DENY_EXACT = [
  '/build.mjs',
  '/package.json',
  '/package-lock.json',
  '/.mcp.json',
];

// Source, config and documentation extensions that have no business being
// fetched from the web root. `.html` is deliberately NOT here — the site is
// HTML. Nor is `.json`: manifest.json and friends are legitimate.
const DENY_SUFFIXES = ['.md', '.mjs', '.ts', '.map', '.bak', '.orig', '.swp', '.yml', '.yaml'];

function isDenied(pathname) {
  const p = pathname.toLowerCase();
  if (isHiddenPath(p)) return true;
  if (DENY_PREFIXES.some((prefix) => p.startsWith(prefix))) return true;
  if (DENY_EXACT.includes(p)) return true;
  if (DENY_SUFFIXES.some((ext) => p.endsWith(ext))) return true;
  return false;
}

// Origins allowed to read responses from the /api proxy. The site's own calls
// are same-origin and need no CORS at all, so this only governs third parties.
// Previously this was `*`, which let any site on the internet use the proxy and
// read authenticated responses (the proxy forwards the Authorization header).
const ALLOWED_ORIGINS = [
  'https://aiphantomtraders.com',
  'https://www.aiphantomtraders.com',
];

function allowOrigin(request) {
  const origin = request.headers.get('Origin');
  if (!origin) return null;
  if (ALLOWED_ORIGINS.includes(origin)) return origin;
  // Cloudflare Pages preview deployments.
  try {
    if (new URL(origin).hostname.endsWith('.pages.dev')) return origin;
  } catch (_) { /* malformed Origin header */ }
  return null;
}

function corsHeaders(request, headers = new Headers()) {
  const origin = allowOrigin(request);
  if (origin) {
    headers.set('Access-Control-Allow-Origin', origin);
    headers.set('Vary', 'Origin');
    headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    headers.set('Access-Control-Allow-Headers', 'Authorization, Content-Type');
    headers.set('Access-Control-Max-Age', '86400');
  }
  return headers;
}

export async function onRequest(context) {
  const { request, next } = context;
  const url = new URL(request.url);

  // 404 rather than 403: don't confirm that a blocked path exists.
  if (isDenied(url.pathname)) {
    return new Response('Not Found', {
      status: 404,
      headers: { 'Content-Type': 'text/plain; charset=utf-8' },
    });
  }

  if (url.pathname.startsWith('/api/')) {
    const backendUrl = 'https://phantom-traders-backend.onrender.com' +
                       url.pathname.replace('/api', '') +
                       url.search;

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 200, headers: corsHeaders(request) });
    }

    const proxyRequest = new Request(backendUrl, {
      method: request.method,
      headers: request.headers,
      body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : null,
    });

    const response = await fetch(proxyRequest);

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: corsHeaders(request, new Headers(response.headers)),
    });
  }

  return next();
}
