// Boutique des originaux : panier (stockage local), compteur dans l'en-tête, page panier et commande.
// Le paiement passe par CHECKOUT_URL (Stripe, Snipcart…) quand il est configuré ; sinon mode démonstration.
(function () {
  var KEY = 'gdo-cart';
  var cfg = window.GDO || {};
  var read = function () { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } };
  var write = function (ids) { try { localStorage.setItem(KEY, JSON.stringify(ids)); } catch (e) {} render(); };
  var products = cfg.products || {};

  // Une œuvre originale est unique : jamais deux fois dans le panier, jamais si elle est vendue.
  var clean = function (ids) { return ids.filter(function (id, i) { return products[id] && !products[id].sold && ids.indexOf(id) === i; }); };

  function render() {
    var ids = clean(read());
    document.querySelectorAll('[data-cart-count]').forEach(function (el) { el.textContent = ids.length ? ' (' + ids.length + ')' : ''; });
    document.querySelectorAll('[data-add]').forEach(function (b) {
      var inCart = ids.indexOf(b.getAttribute('data-add')) > -1;
      b.textContent = inCart ? cfg.t.inCart : cfg.t.addCart;
      b.classList.toggle('is-in', inCart);
    });
    if (document.getElementById('cart')) renderCart(ids);
  }

  // Ajout au panier depuis la galerie
  var toast;
  var say = function (html) {
    if (!toast) { toast = document.createElement('div'); toast.className = 'toast'; toast.setAttribute('role', 'status'); document.body.appendChild(toast); }
    toast.innerHTML = html; toast.hidden = false;
    clearTimeout(toast._t); toast._t = setTimeout(function () { toast.hidden = true; }, 4000);
  };
  document.addEventListener('click', function (e) {
    var add = e.target.closest('[data-add]');
    var now = e.target.closest('[data-buy-now]');
    if (add) {
      var id = add.getAttribute('data-add'), ids = read();
      if (ids.indexOf(id) > -1) { location.href = cfg.cartUrl; return; }
      ids.push(id); write(ids);
      say('<span>' + cfg.t.added + '</span> <a href="' + cfg.cartUrl + '">' + cfg.t.seeCart + '</a>');
    }
    if (now) {
      var nid = now.getAttribute('data-buy-now'), list = read();
      if (list.indexOf(nid) < 0) { list.push(nid); write(list); }
      location.href = cfg.cartUrl + '#commande';
    }
  });

  // ── Page panier ──
  function money(n) { return new Intl.NumberFormat(cfg.locale, { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 }).format(n).replace(/ /g, ' '); }

  function renderCart(ids) {
    var box = document.getElementById('cart');
    var empty = document.getElementById('cart-empty');
    var full = document.getElementById('cart-full');
    empty.hidden = ids.length > 0;
    full.hidden = ids.length === 0;
    if (!ids.length) return;
    box.innerHTML = ids.map(function (id) {
      var p = products[id];
      return '<li class="cart-item"><img src="' + p.img + '" alt="" width="96" height="120">' +
        '<div><h3>' + p.title + '</h3><p>' + p.meta + '</p><p class="unique">' + cfg.t.unique + '</p></div>' +
        '<div class="cart-right"><strong class="price">' + money(p.price) + '</strong>' +
        '<button type="button" class="link" data-remove="' + id + '">' + cfg.t.remove + '</button></div></li>';
    }).join('');
    totals(ids);
  }

  function totals(ids) {
    var sub = ids.reduce(function (s, id) { return s + products[id].price; }, 0);
    var opt = document.querySelector('input[name="delivery"]:checked');
    var ship = opt ? Number(opt.getAttribute('data-price')) : 0;
    document.getElementById('sum-sub').textContent = money(sub);
    document.getElementById('sum-ship').textContent = ship ? money(ship) : cfg.t.free;
    document.getElementById('sum-total').textContent = money(sub + ship);
    document.getElementById('pay-amount').textContent = money(sub + ship);
  }

  document.addEventListener('click', function (e) {
    var rm = e.target.closest('[data-remove]');
    if (rm) write(read().filter(function (x) { return x !== rm.getAttribute('data-remove'); }));
  });
  document.addEventListener('change', function (e) {
    if (e.target.name === 'delivery') {
      totals(clean(read()));
      var pickup = e.target.value === 'pickup';
      document.querySelectorAll('[data-address]').forEach(function (f) { f.hidden = pickup; f.querySelector('input').required = !pickup; });
    }
  });

  var form = document.getElementById('checkout');
  if (form) {
    var rules = {
      name: function (v) { return v.trim().length > 1; },
      email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()); },
      address: function (v) { return v.trim().length > 3; },
      zip: function (v) { return v.trim().length > 1; },
      city: function (v) { return v.trim().length > 1; },
    };
    var check = function (name) {
      var input = form.elements[name], field = input.closest('.field');
      if (field.hidden) return true;
      var ok = rules[name](input.value);
      field.classList.toggle('is-invalid', !ok);
      field.querySelector('.error').hidden = ok;
      input.setAttribute('aria-invalid', String(!ok));
      return ok;
    };
    form.addEventListener('input', function (e) { var f = e.target.closest('.field'); if (f && f.classList.contains('is-invalid')) check(e.target.name); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = Object.keys(rules).filter(function (n) { return !check(n); });
      if (bad.length) { form.elements[bad[0]].focus(); return; }
      var ids = clean(read());
      if (!ids.length) return;
      if (cfg.checkoutUrl) {
        // Paiement réel : on transmet le panier au prestataire (Stripe Checkout, Snipcart…)
        location.href = cfg.checkoutUrl + '?items=' + encodeURIComponent(ids.join(',')) + '&email=' + encodeURIComponent(form.elements.email.value);
        return;
      }
      var n = 'GDO-' + Date.now().toString().slice(-6);
      document.getElementById('order-number').textContent = n;
      document.getElementById('cart-full').hidden = true;
      document.getElementById('order-done').hidden = false;
      try { localStorage.removeItem(KEY); } catch (err) {}
      document.querySelectorAll('[data-cart-count]').forEach(function (el) { el.textContent = ''; });
      window.scrollTo(0, 0);
    });
  }

  render();
})();
