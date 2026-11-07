"""Checks on the built site in _site/ (run `python tools/build_site.py` first).

Usage: python -m unittest tools/test_site.py -v
Standard library only.
"""
import hashlib
import re
import subprocess
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
DOCS = SITE / "docs"
NAV_FILE = ROOT / "docs-src" / "data" / "nav.yaml"
EXCLUDED_PREFIXES = ("docs-src/", "tools/", ".github/")
VERSION = "1.3.0.0"

PAGES = [
    "install", "free-vs-premium",
    "hover-scrub", "video-covers", "folder-thumbnails", "img-slideshow", "vertical-videos",
    "tabs-and-navigation", "search", "sort-and-views", "favorites-and-quick-views", "video-player",
    "drag-into-your-editor",
    "tags",
    "quality-and-speed", "update-and-regenerate", "failed-and-corrupted",
    "libraries", "nas-and-external-drives", "backup-and-move-library",
    "settings", "keyboard-and-mouse", "formats-and-file-names", "troubleshooting",
]
ALL_PAGES = [""] + PAGES  # "" is the docs home, /docs/


def page_file(slug):
    return DOCS / slug / "index.html" if slug else DOCS / "index.html"


def read(path):
    return path.read_text(encoding="utf-8")


def read_nav():
    """Minimal reader for docs-src/data/nav.yaml: `- group: X` followed by `pages: [a, b]`."""
    groups = []
    for line in read(NAV_FILE).splitlines():
        line = line.strip()
        if line.startswith("- group:"):
            groups.append({"group": line.split(":", 1)[1].strip().strip('"'), "pages": []})
        elif line.startswith("pages:"):
            inner = line.split(":", 1)[1].strip().strip("[]")
            groups[-1]["pages"] = [p.strip() for p in inner.split(",") if p.strip()]
    return groups


def marketing_files():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    names = [n for n in out.decode("utf-8").split("\0") if n]
    return [n for n in names if not n.startswith(EXCLUDED_PREFIXES)]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Page(HTMLParser):
    """Collects what the tests need from one HTML file."""

    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.metas = {}
        self.links = []          # (rel, href)
        self.urls = []           # (tag, attr, value) for href/src/poster
        self.imgs = []           # attrs dicts
        self.videos = []         # attrs dicts
        self.sidebar_links = []  # attrs dicts of <a> inside <aside class="sidebar">
        self.sidebar_count = 0
        self.tags = []           # (tag, attrs dict) for every start tag
        self.text = []
        self.main_text = []
        self._stack = []
        self._skip = 0
        self._in_title = False
        self.feed(html)

    def _inside(self, tag, cls=None):
        for t, c in self._stack:
            if t == tag and (cls is None or cls in c.split()):
                return True
        return False

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        self.tags.append((tag, a))
        if tag == "aside" and "sidebar" in a.get("class", "").split():
            self.sidebar_count += 1
        if tag not in self.VOID:
            self._stack.append((tag, a.get("class", "")))
        if tag in ("script", "style", "template"):
            self._skip += 1
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.metas[key] = a.get("content", "")
        if tag == "link":
            self.links.append((a.get("rel", ""), a.get("href", "")))
        for attr in ("href", "src", "poster"):
            if attr in a:
                self.urls.append((tag, attr, a[attr]))
        if tag == "img":
            self.imgs.append(a)
        if tag == "video":
            self.videos.append(a)
        if tag == "a" and self._inside("aside", "sidebar"):
            self.sidebar_links.append(a)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID and self._stack and self._stack[-1][0] == tag:
            self._stack.pop()

    def handle_endtag(self, tag):
        if tag in ("script", "style", "template") and self._skip:
            self._skip -= 1
        if tag == "title":
            self._in_title = False
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i][0] == tag:
                del self._stack[i:]
                break

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._skip:
            return
        self.text.append(data)
        if self._inside("main"):
            self.main_text.append(data)


def parse(path):
    return Page(read(path))


def docs_html_files():
    return sorted(DOCS.rglob("*.html"))


def resolve(page_path, url):
    """Map an internal URL found in page_path to a file under _site, or None for external URLs."""
    if url.startswith(("mailto:", "tel:", "data:", "javascript:", "#")) or not url:
        return None
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return None
    path = unquote(parts.path)
    if not path:
        return None
    if path.startswith("/"):
        target = SITE / path.lstrip("/")
    else:
        target = (page_path.parent / path).resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


class SiteTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if not DOCS.is_dir():
            raise AssertionError("_site/docs is missing: run `python tools/build_site.py` first")

    def test_marketing_files_are_byte_identical(self):
        files = marketing_files()
        self.assertGreater(len(files), 10)
        for name in files:
            with self.subTest(file=name):
                built = SITE / name
                self.assertTrue(built.is_file(), f"{name} missing from _site")
                self.assertEqual(sha256(ROOT / name), sha256(built), f"{name} differs in _site")

    def test_every_page_is_built(self):
        for slug in ALL_PAGES:
            with self.subTest(slug=slug):
                self.assertTrue(page_file(slug).is_file(), f"/docs/{slug} not built")

    def test_sidebar_is_server_rendered(self):
        nav_slugs = [s for g in read_nav() for s in g["pages"]]
        self.assertEqual(sorted(nav_slugs), sorted(PAGES), "nav.yaml and PAGES disagree")
        for slug in ALL_PAGES:
            with self.subTest(slug=slug):
                page = parse(page_file(slug))
                self.assertEqual(page.sidebar_count, 1, 'expected one <aside class="sidebar">')
                hrefs = [a.get("href", "") for a in page.sidebar_links]
                for nav_slug in nav_slugs:
                    hits = [h for h in hrefs if h.rstrip("/").endswith("/docs/" + nav_slug)]
                    self.assertEqual(len(hits), 1, f"sidebar link to {nav_slug}")
                current = [a.get("href", "") for a in page.sidebar_links if a.get("aria-current") == "page"]
                if slug:
                    self.assertEqual(len(current), 1, "exactly one aria-current link")
                    self.assertTrue(current[0].endswith(f"/docs/{slug}/"), current[0])
                else:
                    self.assertEqual(current, [], "the docs home has no current sidebar page")

    def test_head_metadata(self):
        for slug in ALL_PAGES:
            with self.subTest(slug=slug):
                page = parse(page_file(slug))
                url = f"https://reelio.ch/docs/{slug + '/' if slug else ''}"
                self.assertTrue(page.title.strip(), "empty <title>")
                self.assertTrue(page.metas.get("description", "").strip(), "meta description")
                canon = [h for rel, h in page.links if rel == "canonical"]
                self.assertEqual(canon, [url])
                self.assertTrue(page.metas.get("og:title", "").strip(), "og:title")
                self.assertTrue(page.metas.get("og:description", "").strip(), "og:description")
                self.assertEqual(page.metas.get("og:url"), url)

    def test_internal_links_resolve(self):
        files = docs_html_files()
        self.assertTrue(files)
        for path in files:
            page = parse(path)
            for tag, attr, url in page.urls:
                target = resolve(path, url)
                if target is None:
                    continue
                with self.subTest(page=str(path.relative_to(SITE)), url=url):
                    self.assertTrue(target.is_file(), f"<{tag} {attr}={url}> does not resolve")

    def test_no_pending_links(self):
        # a sidebar entry or a /docs/ link whose page is not written yet renders as plain text; none may ship
        for path in docs_html_files():
            with self.subTest(page=str(path.relative_to(SITE))):
                classes = [a.get("class", "").split() for _, a in parse(path).tags]
                self.assertFalse([c for c in classes if "pending" in c or "pending-link" in c])

    def test_no_em_dash_in_docs(self):
        for path in docs_html_files():
            with self.subTest(page=str(path.relative_to(SITE))):
                text = "".join(parse(path).text)
                self.assertNotIn("—", text)

    def test_no_google_fonts(self):
        for path in DOCS.rglob("*"):
            if path.is_file() and path.suffix in (".html", ".css", ".js", ".xml"):
                body = path.read_text(encoding="utf-8", errors="replace")
                with self.subTest(file=str(path.relative_to(SITE))):
                    self.assertNotIn("fonts.googleapis.com", body)
                    self.assertNotIn("fonts.gstatic.com", body)

    def test_images_have_alt(self):
        for path in docs_html_files():
            for img in parse(path).imgs:
                with self.subTest(page=str(path.relative_to(SITE)), src=img.get("src")):
                    self.assertIn("alt", img)
                    if not img["alt"].strip():
                        self.assertEqual(img.get("aria-hidden"), "true", 'alt="" needs aria-hidden="true"')

    def test_no_video_autoplays(self):
        for path in docs_html_files():
            for video in parse(path).videos:
                with self.subTest(page=str(path.relative_to(SITE))):
                    self.assertNotIn("autoplay", video)

    def test_media_weight(self):
        for path in DOCS.rglob("*"):
            if not path.is_file():
                continue
            ext = path.suffix.lower()
            with self.subTest(file=str(path.relative_to(SITE))):
                self.assertNotEqual(ext, ".gif", "no GIF")
                if ext in (".webp", ".jpg", ".jpeg", ".png"):
                    self.assertLessEqual(path.stat().st_size, 400 * 1024)
                if ext in (".mp4", ".webm"):
                    self.assertLessEqual(path.stat().st_size, 2 * 1024 * 1024)

    def test_feature_pages_are_not_skeletons(self):
        for slug in PAGES:
            with self.subTest(slug=slug):
                words = re.findall(r"\w+", " ".join(parse(page_file(slug)).main_text))
                self.assertGreaterEqual(len(words), 150)

    def test_verified_version_shown(self):
        for slug in PAGES:
            with self.subTest(slug=slug):
                text = " ".join(" ".join(parse(page_file(slug)).text).split())
                self.assertIn(f"Verified with Reelio {VERSION}", text)

    def test_shortcodes_render(self):
        path = page_file("hover-scrub")
        page = parse(path)

        def with_class(*classes):
            return [a for _, a in page.tags if set(classes) <= set(a.get("class", "").split())]

        self.assertEqual(len(with_class("callout", "tip")), 1, "one TIP callout")
        self.assertEqual(len(with_class("kbd-table")), 1, "one shortcut table")
        self.assertGreaterEqual(sum(1 for t, _ in page.tags if t == "kbd"), 1, "at least one <kbd>")
        demos = [a for _, a in page.tags if a.get("data-demo") == "scrub"]
        self.assertEqual(len(demos), 1, 'one [data-demo="scrub"]')
        frames = [f for f in demos[0].get("data-frames", "").split(",") if f]
        self.assertEqual(len(frames), 8, "eight scrub frames")
        for url in frames:
            with self.subTest(frame=url):
                self.assertTrue(resolve(path, url).is_file(), f"{url} does not resolve")

    def test_docs_sitemap_and_robots(self):
        sitemap = read(DOCS / "sitemap.xml")
        for slug in PAGES:
            with self.subTest(slug=slug):
                self.assertIn(f"<loc>https://reelio.ch/docs/{slug}/</loc>", sitemap)
        robots = read(SITE / "robots.txt")
        self.assertIn("Sitemap: https://reelio.ch/docs/sitemap.xml", robots)
        self.assertIn("Sitemap: https://reelio.ch/sitemap.xml", robots)


if __name__ == "__main__":
    unittest.main()
