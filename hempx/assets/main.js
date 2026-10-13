/* HempX – közös szkript */

// ── Hírlevél-feliratkozás linkje ──────────────────────────────────────────
// Illeszd be ide a Mailchimp "Signup forms" → "Form builder / Embedded & hosted forms" oldalán
// található nyilvános feliratkozási linket (pl. https://eepurl.com/xxxxx).
// Amíg ez üres, a gomb e-mailes feliratkozásra esik vissza.
var NEWSLETTER_URL = '';

(function () {
  var FALLBACK = 'mailto:hempx2025@gmail.com?subject=H%C3%ADrlev%C3%A9l%20feliratkoz%C3%A1s';
  document.querySelectorAll('.js-news').forEach(function (a) {
    a.href = NEWSLETTER_URL || FALLBACK;
    if (NEWSLETTER_URL) { a.target = '_blank'; a.rel = 'noopener'; }
  });

  // mobil menü
  var burger = document.getElementById('burger'), menu = document.getElementById('mobileMenu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var o = menu.classList.toggle('open');
      burger.classList.toggle('open', o);
      burger.setAttribute('aria-expanded', o ? 'true' : 'false');
      document.body.style.overflow = o ? 'hidden' : '';
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.remove('open'); burger.classList.remove('open'); document.body.style.overflow = '';
      });
    });
  }

  // reveal
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // GYIK
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.parentElement, a = item.querySelector('.faq-a'), open = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(function (it) {
        it.classList.remove('open'); it.querySelector('.faq-a').style.maxHeight = null;
        it.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
      });
      if (!open) { item.classList.add('open'); a.style.maxHeight = a.scrollHeight + 'px'; q.setAttribute('aria-expanded', 'true'); }
    });
  });

  // HU ⇄ EN
  var KEY = 'hempx-lang';
  var textEls = document.querySelectorAll('[data-en]');
  textEls.forEach(function (el) { el.dataset.hu = el.innerHTML; });
  var toggles = document.querySelectorAll('.lang');
  var META = window.HEMPX_META || null;
  function apply(lang) {
    document.documentElement.lang = lang;
    textEls.forEach(function (el) { el.innerHTML = lang === 'en' ? el.dataset.en : el.dataset.hu; });
    if (META && META[lang]) {
      document.title = META[lang].title;
      var d = document.querySelector('meta[name="description"]'); if (d) d.content = META[lang].desc;
    }
    toggles.forEach(function (b) {
      b.textContent = lang === 'en' ? 'HU' : 'EN';
      b.setAttribute('aria-label', lang === 'en' ? 'Váltás magyarra' : 'Switch to English');
    });
    try { localStorage.setItem(KEY, lang); } catch (e) {}
    document.querySelectorAll('.faq-item.open .faq-a').forEach(function (a) { a.style.maxHeight = a.scrollHeight + 'px'; });
  }
  toggles.forEach(function (b) {
    b.addEventListener('click', function () { apply(document.documentElement.lang === 'en' ? 'hu' : 'en'); });
  });
  var init = 'hu';
  try { var s = localStorage.getItem(KEY); if (s === 'en' || s === 'hu') init = s; } catch (e) {}
  if (init === 'en') apply('en');
})();
