/* Reelio docs: mobile drawer, carousel, clips. No dependencies. */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- mobile drawer ---- */
  (function drawer() {
    var toggle = document.getElementById('menuToggle');
    var scrim = document.getElementById('scrim');
    var sidebar = document.getElementById('sidebar');
    if (!toggle || !sidebar) return;
    function isOpen() { return document.body.classList.contains('nav-open'); }
    function close(returnFocus) {
      if (!isOpen()) return;
      document.body.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
      if (returnFocus) toggle.focus();
    }
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', String(open));
      if (open) {
        var first = sidebar.querySelector('a[aria-current="page"]') || sidebar.querySelector('a');
        if (first) first.focus({ preventScroll: true });
      }
    });
    if (scrim) scrim.addEventListener('click', function () { close(false); });
    sidebar.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { close(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close(true);
    });
    var wide = window.matchMedia('(min-width: 821px)');
    wide.addEventListener('change', function (e) { if (e.matches) close(false); });
  })();

  /* ---- carousels (only on pages that have one) ---- */
  document.querySelectorAll('[data-carousel]').forEach(function (root) {
    var track = root.querySelector('.carousel-track');
    var slides = Array.prototype.slice.call(root.querySelectorAll('.carousel-slide'));
    var dots = Array.prototype.slice.call(root.querySelectorAll('.carousel-dots button'));
    var i = 0;
    function go(n) {
      i = (n + slides.length) % slides.length;
      track.style.transform = 'translateX(' + (-i * 100) + '%)';
      slides.forEach(function (s, k) { s.setAttribute('aria-hidden', String(k !== i)); });
      dots.forEach(function (d, k) {
        d.classList.toggle('active', k === i);
        d.setAttribute('aria-current', k === i ? 'true' : 'false');
      });
    }
    dots.forEach(function (d, k) { d.addEventListener('click', function () { go(k); }); });
    root.querySelector('.prev').addEventListener('click', function () { go(i - 1); });
    root.querySelector('.next').addEventListener('click', function () { go(i + 1); });
    root.setAttribute('tabindex', '0');
    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { go(i - 1); e.preventDefault(); }
      if (e.key === 'ArrowRight') { go(i + 1); e.preventDefault(); }
    });
    var startX = null;
    track.addEventListener('pointerdown', function (e) { startX = e.clientX; });
    track.addEventListener('pointerup', function (e) {
      if (startX === null) return;
      var dx = e.clientX - startX;
      startX = null;
      if (Math.abs(dx) > 40) go(dx < 0 ? i + 1 : i - 1);
    });
    go(0);
  });

  /* ---- clips: play when visible, never with reduced motion; a button always toggles ---- */
  document.querySelectorAll('[data-clip]').forEach(function (root) {
    var video = root.querySelector('video');
    var button = root.querySelector('.clip-toggle');
    var label = button.querySelector('span');
    var icon = button.querySelector('path');
    var userPaused = false;
    function render() {
      var playing = !video.paused;
      button.setAttribute('aria-pressed', String(playing));
      label.textContent = playing ? 'Pause' : 'Play';
      icon.setAttribute('d', playing ? 'M4 2.5h3v11H4zM9 2.5h3v11H9z' : 'M4 2.5v11l9-5.5z');
    }
    function play() { var p = video.play(); if (p && p.catch) p.catch(function () {}); }
    video.addEventListener('play', render);
    video.addEventListener('pause', render);
    button.addEventListener('click', function () {
      if (video.paused) { userPaused = false; play(); } else { userPaused = true; video.pause(); }
    });
    if (reducedMotion || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { if (!userPaused) play(); } else if (!video.paused) { video.pause(); }
      });
    }, { threshold: 0.5 }).observe(root);
  });
})();
