"""Build the whole site into _site/: the marketing site as-is, plus the Hugo docs in _site/docs/.

Usage: python tools/build_site.py
Used both locally and by the GitHub Pages workflow. Standard library only.
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
DOCS_SRC = ROOT / "docs-src"
EXCLUDED_PREFIXES = ("docs-src/", "tools/", ".github/")
INSTALL_HINT = "Hugo not found. Install it with: winget install Hugo.Hugo.Extended"


def tracked_marketing_files():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    names = [n for n in out.decode("utf-8").split("\0") if n]
    return [n for n in names if not n.startswith(EXCLUDED_PREFIXES)]


def copy_marketing_site():
    count = 0
    for name in tracked_marketing_files():
        src = ROOT / name
        if not src.is_file():
            continue  # deleted in the working tree but still in the index
        dest = SITE / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        count += 1
    return count


def check_hugo_version(hugo):
    wanted = (DOCS_SRC / ".hugo-version").read_text(encoding="utf-8").strip()
    found = subprocess.run([hugo, "version"], capture_output=True, text=True, check=True).stdout.strip()
    if f"v{wanted}" not in found:
        print(f"WARNING: docs-src/.hugo-version pins {wanted}, but `hugo version` says: {found}", file=sys.stderr)


def main():
    hugo = shutil.which("hugo")
    if hugo is None:
        print(INSTALL_HINT, file=sys.stderr)
        return 1
    check_hugo_version(hugo)
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    count = copy_marketing_site()
    print(f"Copied {count} marketing files to _site/")
    result = subprocess.run([hugo, "--source", str(DOCS_SRC), "--destination", str(SITE / "docs"),
                             "--minify", "--panicOnWarning", "--cleanDestinationDir"])
    if result.returncode != 0:
        print("Hugo build failed", file=sys.stderr)
        return result.returncode
    print("Built the docs into _site/docs/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
