# Reelio — Landing Page

Production static implementation of the **Reelio** marketing landing page, built from the
Claude Design handoff bundle (`Reelio-handoff/`). Reelio is a native Windows video-library
manager with hover-scrub previews, color tags, FTS5 search and drag-into-editor.

The handoff prototype was a single self-contained `Reelio Landing Page.html`. This repo splits
it into a clean, deployable static site with **byte-for-byte identical** CSS and JS (verified —
see [Fidelity](#fidelity)), plus production hygiene the prototype didn't ship (external assets,
social card, robots/sitemap/manifest).

## Structure

```
.
├── index.html          # The page (semantic markup + SEO/OG/Twitter meta + JSON-LD)
├── styles.css          # All styles (design tokens + every section) — extracted from the prototype
├── script.js           # Hover-scrub previews, cursor hint, walk-through hotspots
├── assets/             # Images & SVGs; includes generated og-image.png (1200×630)
├── favicon.ico         # Multi-size icon so the root /favicon.ico request resolves
├── robots.txt          # Allow all + sitemap pointer
├── sitemap.xml         # Single-page sitemap (https://reelio.app/)
├── site.webmanifest    # Web app manifest (name, theme color, icons)
└── Reelio-handoff/      # Original design bundle, kept for reference (not deployed)
```

## Run it

It's pure static — no build step, no dependencies.

```powershell
# Option A: just open it
start index.html

# Option B: serve locally (recommended — matches production paths)
python -m http.server 8000
# then visit http://localhost:8000
```

Serving over HTTP (Option B) is preferred so root-relative behavior, the Google Fonts
request and lazy-loading all behave exactly as in production.

## Deploy

Drop the repo root onto any static host — Netlify, Cloudflare Pages, GitHub Pages, S3 +
CloudFront, etc. No configuration required. The canonical URL, Open Graph, Twitter card,
`robots.txt` and `sitemap.xml` are all wired for **https://reelio.app/**; change that domain
in `index.html` (canonical, `og:url`, `og:image`, `twitter:image`, JSON-LD `url`/`image`),
`robots.txt` and `sitemap.xml` if you deploy elsewhere.

## Tech

- **HTML/CSS/JS**, zero framework, zero build.
- Fonts: Bricolage Grotesque, Geist, JetBrains Mono via Google Fonts (`preconnect` + `display=swap`).
- Interactions (all in `script.js`, progressive-enhancement — page is fully readable without JS):
  - **Hover-scrub previews** — moving the mouse across a `.video-frame` scrubs through frame
    images; segment bar + frame index track the cursor. Touch-friendly.
  - **Cursor hint** — a one-time slide-across nudge on the hero preview until first hover
    (remembered per session via `sessionStorage`); respects `prefers-reduced-motion`.
  - **Walk-through hotspots** — pulsing dots over the app screenshot auto-cycle their tooltips,
    pause on hover, and only run while scrolled into view (IntersectionObserver).

## Fidelity

The recreation is **pixel-perfect by construction**, verified in two stages:

1. **Split** — the page was first split mechanically, so re-inlining `styles.css` + `script.js`
   back into `index.html` reproduced the prototype **byte-for-byte** (identical SHA-256). The
   inline `<style>` became `<link rel="stylesheet">`, the inline `<script>` became
   `<script src>`, and the two `application/ld+json` blocks stayed inline in `<head>`.
2. **Hardening** — production fixes were then layered on. Stripping those documented additions
   back out leaves the `<body>` markup, CSS and JS **byte-identical to the original** — i.e. the
   rendered design is provably unchanged. The fixes only affect metadata, structured data, and
   states the default mouse user never sees (reduced-motion, keyboard focus, decode/layout hints).

### Production hardening applied (all visually neutral)

- **SEO / structured data** — corrected the FAQ JSON-LD to mirror the visible Q&A verbatim;
  added `robots`, `og:image:width/height/alt`, `twitter:image:alt`; tightened the meta
  description to fit the search-results window.
- **Social / icons** — generated `assets/og-image.png` (1200×630), a multi-size `favicon.ico`,
  an `apple-touch-icon`, and linked `site.webmanifest`.
- **Performance** — intrinsic `width`/`height` on raster `<img>`s (kills layout shift),
  `decoding="async"`, and a `<link rel="preload" fetchpriority="high">` for the hero LCP image.
- **Accessibility** — a `prefers-reduced-motion` guard that pauses the marquee, a keyboard
  `:focus-visible` ring, hover-spot tooltips that now also show on keyboard focus, and a
  "Label in Name" fix on the first hotspot's `aria-label`.

## Needs your input (intentionally NOT changed)

These are real but require a decision or asset only you can provide:

1. **Price in structured data** — the `SoftwareApplication` JSON-LD still advertises
   `"price": "14.99" USD`, but no price appears on the page (copy says only "one-time payment").
   Either surface the real price on the page, or drop `price`/`priceCurrency` from the markup.
2. **Store link** — the Store CTA buttons (`href="#"`/`#get`) and JSON-LD `downloadUrl`
   (`apps.microsoft.com/`) are placeholders; point them at the real Microsoft Store listing
   once it's live.
3. **Orange brand text contrast** — `--orange #FE9C2E` text on the light background is ~2:1
   (below WCAG AA). Fixing it means darkening the brand orange (a visual/design change), so
   it's left to you.
4. **Image weight** — `assets/` is ~40 MB because the hover-scrub frames ship at full camera
   resolution into ~370 px thumbnails. Lazy-loaded, but downscaling to ~2× the display size +
   WebP would cut ~80–90% with no visible change. Happy to do this as a follow-up.
5. **Hero heading order** — two `<h3>` stat-cards precede the first `<h2>`; a clean fix needs a
   small semantics/CSS tweak, so it's flagged rather than forced.

## Assets

`assets/` is the curated set from the handoff. The page references 48 of them; a handful of
extra handoff images are included but unused by this page (e.g. `app-screenshot.png`,
`fig-dragging-clip.png`, `logo-light.svg`) — safe to prune if you want a leaner deploy.
`assets/og-image.png` is generated (brand-yellow card framing the app screenshot with the
Reelio can-logo chip); replace it with a purpose-built card any time.

### Optimization note

The hover-scrub frame photos (`surf-frame-*`, `surf-b-*`, `surf-c-*`, `scrub-*`,
`fig-hero-thumb.png`) ship at full camera resolution (several are 1–2 MB) but render in small
thumbnails. They are lazy-loaded, but downscaling them to ~2× their display size and/or serving
WebP would cut page weight dramatically. Left as-is here to preserve the handoff assets exactly.
