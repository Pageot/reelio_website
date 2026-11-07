/* Hover-scrub demo. Mirrors Reelio: the tile width is split into N equal zones (N = 2, 3 or 8 by clip length),
   the zone under the pointer picks the frame, and leaving the tile shows the resting (middle) frame again. */
(function () {
  'use strict';

  /* Where the app takes its frames, as fractions of the clip (2: 1/3 and 2/3; 3: 25/50/75%; 8: zone centres). */
  var POSITIONS = {
    2: [1 / 3, 2 / 3],
    3: [0.25, 0.5, 0.75],
    8: [0.0625, 0.1875, 0.3125, 0.4375, 0.5625, 0.6875, 0.8125, 0.9375]
  };

  document.querySelectorAll('[data-demo="scrub"]').forEach(function (root) {
    var sources = root.getAttribute('data-frames').split(',');
    var tile = root.querySelector('.demo-tile');
    var img = root.querySelector('.demo-frame');
    var cap = root.querySelector('.demo-cap');
    var zonesEl = root.querySelector('.demo-zones');
    var buttons = Array.prototype.slice.call(root.querySelectorAll('[data-frames-count]'));
    var count = 8;
    var frames = [];
    var zone = -1;

    sources.forEach(function (src) { var i = new Image(); i.src = src; });

    function pick(n) {
      /* Map each app position onto the 8 demo stills (taken at the 8 zone centres). */
      return POSITIONS[n].map(function (p) { return sources[Math.min(sources.length - 1, Math.floor(p * sources.length))]; });
    }
    function resting() { return Math.floor(count / 2); }

    function renderZones() {
      zonesEl.textContent = '';
      for (var k = 0; k < count; k++) {
        var z = document.createElement('span');
        if (k === zone) z.className = 'on';
        zonesEl.appendChild(z);
      }
    }
    function show(k) {
      zone = k;
      if (k < 0) {
        img.src = frames[resting()];
        cap.textContent = 'Resting image';
      } else {
        img.src = frames[k];
        cap.textContent = 'Frame ' + (k + 1) + ' of ' + count;
      }
      renderZones();
    }
    function setCount(n) {
      count = n;
      frames = pick(n);
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(Number(b.getAttribute('data-frames-count')) === n)); });
      show(-1);
    }
    function zoneAt(clientX) {
      var r = tile.getBoundingClientRect();
      var x = Math.max(0, Math.min(r.width - 0.001, clientX - r.left));
      return Math.floor(x / r.width * count);
    }

    tile.addEventListener('pointermove', function (e) { var k = zoneAt(e.clientX); if (k !== zone) show(k); });
    tile.addEventListener('pointerdown', function (e) { show(zoneAt(e.clientX)); });
    tile.addEventListener('pointerleave', function () { show(-1); });
    tile.addEventListener('pointercancel', function () { show(-1); });
    tile.addEventListener('pointerup', function (e) { if (e.pointerType !== 'mouse') show(-1); });
    tile.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { show(Math.min(count - 1, zone + 1)); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { show(zone <= 0 ? 0 : zone - 1); e.preventDefault(); }
      else if (e.key === 'Escape') { show(-1); }
    });
    tile.addEventListener('blur', function () { show(-1); });
    buttons.forEach(function (b) {
      b.addEventListener('click', function () { setCount(Number(b.getAttribute('data-frames-count'))); });
    });
    setCount(8);
  });
})();
