// ============================================================
// SERVICE WORKER — Konkou Konesans par Septa v1.0
// Cache-First pou statik, Network-First pou API
// ============================================================

const STATIC_CACHE = 'konkou-static-v1';
const API_CACHE    = 'konkou-api-v1';

const PRECACHE_URLS = [
  '/',
  '/static/manifest.json',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png',
  'https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Outfit:wght@300;400;500;600&display=swap',
];

// INSTALL
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then(cache => cache.addAll(PRECACHE_URLS).catch(e => console.warn('[SW] pre-cache warn:', e)))
      .then(() => self.skipWaiting())
  );
});

// ACTIVATE — netwaye vye cache
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== STATIC_CACHE && k !== API_CACHE).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

// FETCH
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  if (url.pathname.startsWith('/api/')) {
    event.respondWith(networkFirst(event.request)); return;
  }
  if (url.hostname.includes('fonts.g') || url.hostname.includes('ui-avatars')) {
    event.respondWith(cacheFirst(event.request)); return;
  }
  if (url.pathname.startsWith('/static/')) {
    event.respondWith(cacheFirst(event.request)); return;
  }
  event.respondWith(networkFirst(event.request));
});

async function cacheFirst(req) {
  const hit = await caches.match(req);
  if (hit) return hit;
  try {
    const res = await fetch(req);
    if (res.ok) { const c = await caches.open(STATIC_CACHE); c.put(req, res.clone()); }
    return res;
  } catch { return new Response('Offline', { status: 503 }); }
}

async function networkFirst(req) {
  try {
    const res = await fetch(req);
    if (res.ok && req.method === 'GET') {
      const c = await caches.open(API_CACHE); c.put(req, res.clone());
    }
    return res;
  } catch {
    const hit = await caches.match(req);
    return hit || new Response(JSON.stringify({error:'Offline'}), {status:503,headers:{'Content-Type':'application/json'}});
  }
}
