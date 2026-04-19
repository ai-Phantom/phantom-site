const CACHE_NAME = 'phantom-v2';
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
  const isHTML = e.request.mode === 'navigate' ||
    (e.request.headers.get('accept') || '').includes('text/html') ||
    url.pathname === '/' || url.pathname.endsWith('.html');
  if (isHTML) {
    e.respondWith(fetch(e.request).catch(() => caches.match('/logo.jpeg')));
    return;
  }
  e.respondWith(
    fetch(e.request)
      .then(r => {
        if (r.ok && r.type === 'basic') {
          const clone = r.clone();
          caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        }
        return r;
      })
      .catch(() => caches.match(e.request))
  );
});
