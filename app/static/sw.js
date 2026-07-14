const CACHE = 'cerveceria-v1';
const FILES = [
  '/',
  '/recetas/',
  '/inventario/',
  '/lotes/',
  '/ventas/',
  '/static/manifest.json'
];

self.addEventListener('install', function(e) {
  e.waitUntil(caches.open(CACHE).then(function(cache) {
    return cache.addAll(FILES);
  }));
});

self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(r) {
      return r || fetch(e.request);
    })
  );
});
