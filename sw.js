const CACHE_NAME = 'phantom-v3';
const SHELL = ['/logo.jpeg', '/manifest.json'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(SHELL)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);

  // Do NOT intercept cross-origin requests. Re-issuing them from the SW
  // runs them under connect-src instead of script-src/img-src/etc., which
  // breaks every third-party script (Supabase CDN, Sentry, GA, Cloudflare
  // Insights...). Let the browser handle them natively.
  if (url.origin !== self.location.origin) return;

  // Same-origin HTML: always go to network. No fallback — we'd rather fail
  // fast than serve a stale shell when the real HTML exists on the origin.
  const isHTML = e.request.mode === 'navigate' ||
    (e.request.headers.get('accept') || '').includes('text/html') ||
    url.pathname === '/' || url.pathname.endsWith('.html');
  if (isHTML) {
    e.respondWith(fetch(e.request));
    return;
  }

  // Same-origin static assets: stale-while-revalidate.
  e.respondWith(
    fetch(e.request)
      .then(r => {
        if (r.ok && r.type === 'basic') {
          const clone = r.clone();
          caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        }
        return r;
      })
      .catch(() => caches.match(e.request).then(c => c || Response.error()))
  );
});
