(function () {
  var views = document.querySelectorAll('.view');
  function show() {
    var id = (location.hash || '').slice(1);
    var target = document.querySelector('.view[data-view="' + id + '"]');
    if (!target) target = document.querySelector('.view[data-view="home"]');
    views.forEach(function (v) { v.hidden = v !== target; });
    document.title = target.dataset.view === 'home'
      ? 'DIGIASIA 2026 講座筆記'
      : (target.querySelector('.who b').textContent + '｜DIGIASIA 2026 講座筆記');
    window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', show);
  show();

  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-jump]');
    if (!a) return;
    e.preventDefault();
    var el = document.getElementById(a.dataset.jump);
    if (!el) return;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
  });

  // highlight current section in tabs
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var id = en.target.id;
        document.querySelectorAll('[data-jump]').forEach(function (a) {
          a.classList.toggle('on', a.dataset.jump === id);
        });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    document.querySelectorAll('.part').forEach(function (s) { io.observe(s); });
  }
})();
(function () {
  var box = document.createElement('button');
  box.type = 'button'; box.className = 'lightbox'; box.hidden = true; box.setAttribute('aria-label', '關閉照片');
  var img = document.createElement('img'); box.appendChild(img); document.body.appendChild(box);
  document.addEventListener('click', function (e) {
    var z = e.target.closest('.zoom');
    if (z) { img.src = z.querySelector('img').src; img.alt = z.querySelector('img').alt; box.hidden = false; box.focus(); return; }
    if (e.target.closest('.lightbox')) box.hidden = true;
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') box.hidden = true; });
})();
