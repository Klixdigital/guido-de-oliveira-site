// Guido De Oliveira : menu mobile, zoom des œuvres, années de la galerie, newsletter.
(function () {
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 4); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Menu mobile
  var btn = document.querySelector('.menu-btn');
  var drawer = document.getElementById('drawer');
  if (btn && drawer) {
    btn.addEventListener('click', function () {
      var open = drawer.hidden;
      drawer.hidden = !open;
      btn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !drawer.hidden) { drawer.hidden = true; btn.setAttribute('aria-expanded', 'false'); btn.focus(); }
    });
  }

  // Retenir la langue choisie (utilisé par la page d'accueil racine)
  document.querySelectorAll('.langs a').forEach(function (a) {
    a.addEventListener('click', function () { try { localStorage.setItem('lang', a.getAttribute('hreflang')); } catch (e) {} });
  });

  // Liens pas encore fournis par l'artiste : on reste sur la page et on le signale.
  var toast;
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-todo]');
    if (!a) return;
    e.preventDefault();
    if (!toast) {
      toast = document.createElement('p');
      toast.setAttribute('role', 'status');
      toast.style.cssText = 'position:fixed;left:50%;bottom:1.5rem;transform:translateX(-50%);z-index:50;margin:0;padding:.8rem 1.2rem;background:#1c1b19;color:#fff;border-radius:2px;font-size:.95rem;box-shadow:0 12px 30px -10px rgba(0,0,0,.5)';
      document.body.appendChild(toast);
    }
    toast.textContent = a.getAttribute('data-todo');
    toast.hidden = false;
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { toast.hidden = true; }, 2600);
  });

  // Zoom des œuvres
  var box = document.querySelector('.lightbox');
  if (box && box.showModal) {
    var img = box.querySelector('img');
    document.querySelectorAll('.zoom[data-full]').forEach(function (z) {
      z.addEventListener('click', function () {
        var thumb = z.querySelector('img');
        img.src = z.getAttribute('data-full');
        img.alt = thumb ? thumb.alt : '';
        box.showModal();
      });
    });
    box.querySelector('button').addEventListener('click', function () { box.close(); });
    box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
  }

  // Galerie : l'année à l'écran est soulignée dans la barre des années
  var yearLinks = document.querySelectorAll('.years a');
  if (yearLinks.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        yearLinks.forEach(function (a) { a.classList.toggle('is-active', a.getAttribute('href') === '#' + en.target.id); });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    document.querySelectorAll('.year').forEach(function (s) { io.observe(s); });
  }

  // Newsletter : contrôle des champs, puis envoi au service choisi (ou par e-mail en attendant).
  document.querySelectorAll('form[data-newsletter]').forEach(function (form) {
    var fields = {
      name: function (v) { return v.trim().length > 1; },
      email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()); },
    };
    var check = function (name) {
      var input = form.elements[name];
      var ok = fields[name](input.value);
      var field = input.closest('.field');
      field.classList.toggle('is-invalid', !ok);
      field.querySelector('.error').hidden = ok;
      input.setAttribute('aria-invalid', String(!ok));
      return ok;
    };
    form.addEventListener('input', function (e) {
      var f = e.target.closest('.field');
      if (f && f.classList.contains('is-invalid')) check(e.target.name);
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var okName = check('name'), okEmail = check('email');
      if (!okName) { form.elements.name.focus(); return; }
      if (!okEmail) { form.elements.email.focus(); return; }
      var done = function () {
        form.querySelector('.form-ok').hidden = false;
        form.querySelector('button[type="submit"]').disabled = true;
      };
      var action = form.getAttribute('data-action');
      var to = form.getAttribute('data-email');
      if (action) {
        fetch(action, { method: 'POST', body: new FormData(form), mode: 'no-cors' }).then(done, done);
      } else if (to) {
        var body = form.elements.name.value + '\n' + form.elements.email.value;
        location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(form.getAttribute('data-subject')) + '&body=' + encodeURIComponent(body);
        done();
      } else {
        done(); // maquette : aucun service branché pour l'instant
      }
    });
  });

  // Vidéo : bascule sur l'emplacement si le fichier manque
  document.querySelectorAll('.video-frame video').forEach(function (v) {
    v.addEventListener('error', function () { v.closest('.video-frame').classList.add('is-missing'); }, true);
  });
})();
