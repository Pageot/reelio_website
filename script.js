(() => {
  const SETS = {
    'hero': [
      'assets/fig-hero-thumb.jpg',
      'assets/scrub-01.jpg',
      'assets/scrub-02.jpg',
      'assets/scrub-03.jpg',
      'assets/scrub-04.jpg',
    ],
    'surf-a': [
      'assets/surf-frame-01.jpg',
      'assets/surf-frame-02.jpg',
      'assets/surf-frame-03.jpg',
      'assets/surf-frame-04.jpg',
      'assets/surf-frame-05.jpg',
      'assets/surf-frame-06.jpg',
      'assets/surf-frame-07.jpg',
      'assets/surf-frame-08.jpg',
    ],
    'surf-b': [
      'assets/surf-b-01.jpg',
      'assets/surf-b-02.jpg',
      'assets/surf-b-03.jpg',
      'assets/surf-b-04.jpg',
      'assets/surf-b-05.jpg',
      'assets/surf-b-06.jpg',
      'assets/surf-b-07.jpg',
      'assets/surf-b-08.jpg',
    ],
    'surf-c': [
      'assets/surf-c-01.jpg',
      'assets/surf-c-02.jpg',
      'assets/surf-c-03.jpg',
      'assets/surf-c-04.jpg',
      'assets/surf-c-05.jpg',
      'assets/surf-c-06.jpg',
      'assets/surf-c-07.jpg',
      'assets/surf-c-08.jpg',
    ],
  };

  function buildScrub(el) {
    const key = el.dataset.frames || 'surf-a';
    const frames = SETS[key] || SETS['surf-a'];
    const stage = el.querySelector('.scrub-stage');
    const segs = el.querySelectorAll('.scrub-segs span');
    const tape = el.querySelector('.scrub-tape');
    const total = frames.length;

    frames.forEach((src, i) => {
      const img = document.createElement('img');
      img.src = src;
      img.alt = '';
      img.loading = 'lazy';
      img.decoding = 'async';
      if (i === 0) img.classList.add('is-on');
      stage.appendChild(img);
    });
    const imgs = stage.querySelectorAll('img');
    if (segs.length) segs[0].classList.add('is-on');
    let cur = 0;

    function set(pct) {
      pct = Math.max(0, Math.min(1, pct));
      const idx = Math.min(total - 1, Math.floor(pct * total));
      const segIdx = Math.min(segs.length - 1, Math.floor(pct * segs.length));
      if (idx !== cur) {
        imgs[cur].classList.remove('is-on');
        imgs[idx].classList.add('is-on');
        cur = idx;
      }
      segs.forEach((s, i) => s.classList.toggle('is-on', i <= segIdx));
      if (tape && pct > 0.04) { tape.style.opacity = '0'; tape.style.transition = 'opacity .2s'; }
    }
    function reset() {
      if (tape) tape.style.opacity = '1';
      set(0);
    }
    function fromEvent(e) {
      const r = el.getBoundingClientRect();
      const x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
      return x / r.width;
    }

    el.addEventListener('mousemove', e => set(fromEvent(e)));
    el.addEventListener('touchmove', e => { set(fromEvent(e)); e.preventDefault(); }, { passive: false });
    el.addEventListener('mouseleave', reset);
  }

  document.querySelectorAll('[data-scrub]').forEach(buildScrub);

  // ===== Cursor hint: slide-across animation until first hover (per session) =====
  (() => {
    const KEY = 'reelio-scrub-hinted';
    const targets = document.querySelectorAll('[data-scrub][data-frames="hero"]');
    if (!targets.length) return;

    // Inject the cursor image inside each target
    targets.forEach((el) => {
      if (el.querySelector('.scrub-cursor')) return;
      const cursor = document.createElement('img');
      cursor.className = 'scrub-cursor';
      cursor.src = 'assets/cursor-hint.svg';
      cursor.alt = '';
      cursor.setAttribute('aria-hidden', 'true');
      el.appendChild(cursor);
    });

    const dismissed = () => {
      try { return sessionStorage.getItem(KEY) === '1'; }
      catch (e) { return false; }
    };
    const dismiss = () => {
      try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
      document.querySelectorAll('.video-frame.show-cursor-hint')
        .forEach(v => v.classList.remove('show-cursor-hint'));
    };

    if (!dismissed()) {
      targets.forEach(el => el.classList.add('show-cursor-hint'));
      const onHover = () => dismiss();
      targets.forEach((el) => {
        el.addEventListener('mouseenter', onHover, { once: true });
        el.addEventListener('touchstart', onHover, { once: true, passive: true });
      });
    }
  })();

  // ===== Walk-through hotspots: auto-cycle + pause on hover =====
  (() => {
    const root = document.getElementById('walk-shot');
    if (!root) return;
    const spots = Array.from(root.querySelectorAll('.walk-spot'));
    if (!spots.length) return;
    let idx = 0;
    let timer = null;
    let paused = false;

    const setActive = (i) => {
      spots.forEach((s, j) => s.classList.toggle('is-active', j === i));
    };

    const tick = () => {
      if (paused) return;
      idx = (idx + 1) % spots.length;
      setActive(idx);
    };

    const start = () => {
      if (timer) return;
      setActive(idx);
      timer = setInterval(tick, 5000);
    };
    const stop = () => {
      if (timer) clearInterval(timer);
      timer = null;
      spots.forEach((s) => s.classList.remove('is-active'));
    };

    root.addEventListener('mouseenter', () => { paused = true; stop(); });
    root.addEventListener('mouseleave', () => { paused = false; start(); });

    // Start cycling when scrolled into view (saves work off-screen)
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) start();
          else stop();
        });
      }, { threshold: 0.2 });
      io.observe(root);
    } else {
      start();
    }
  })();
})();
