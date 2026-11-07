#!/usr/bin/env python3
"""
fetch_images.py - Download all external images used in index.html into ./images/
and rewrite index.html to use the local copies.

Run once from the site folder before going live:
    python3 fetch_images.py

Needs only the Python standard library (Python 3.8+).
A backup of the original page is saved as index.html.bak.
"""

import os
import re
import shutil
import sys
import urllib.request

PAGE = "index.html"
IMG_DIR = "images"

# Remote URL -> local file name
IMAGES = {
    "https://images.pexels.com/photos/7168457/pexels-photo-7168457.jpeg?auto=compress&cs=tinysrgb&w=1800": "hero-construction.jpg",
    "https://images.pexels.com/photos/8960992/pexels-photo-8960992.jpeg?auto=compress&cs=tinysrgb&w=1000": "mission.jpg",
    "https://images.pexels.com/photos/5811993/pexels-photo-5811993.jpeg?auto=compress&cs=tinysrgb&w=800": "value-quality.jpg",
    "https://images.pexels.com/photos/34670930/pexels-photo-34670930/free-photo-of-construction-workers-in-safety-gear-at-site.jpeg?auto=compress&cs=tinysrgb&w=800": "value-transparency.jpg",
    "https://images.pexels.com/photos/8961156/pexels-photo-8961156.jpeg?auto=compress&cs=tinysrgb&w=800": "value-workmanship.jpg",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (site image fetcher)"}


def download(url: str, dest: str) -> bool:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest, "wb") as out:
            shutil.copyfileobj(resp, out)
        size_kb = os.path.getsize(dest) // 1024
        if size_kb < 5:
            print(f"  WARNING: {dest} is only {size_kb} KB - check it opens correctly")
        else:
            print(f"  OK  {dest} ({size_kb} KB)")
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"  FAIL {url}\n       {exc}")
        return False


def main() -> int:
    if not os.path.exists(PAGE):
        print(f"Run this script from the folder that contains {PAGE}.")
        return 1

    os.makedirs(IMG_DIR, exist_ok=True)

    with open(PAGE, encoding="utf-8") as f:
        html = f.read()

    shutil.copyfile(PAGE, PAGE + ".bak")
    print(f"Backup saved: {PAGE}.bak\nDownloading {len(IMAGES)} images...")

    failed = 0
    for url, name in IMAGES.items():
        local = f"{IMG_DIR}/{name}"
        if url not in html:
            print(f"  SKIP (not in page) {name}")
            continue
        if download(url, local):
            html = html.replace(url, local)
        else:
            failed += 1

    with open(PAGE, "w", encoding="utf-8") as f:
        f.write(html)

    leftovers = re.findall(r'https://images\.pexels\.com[^"\')\s]+', html)
    print("\nDone.")
    if failed or leftovers:
        print(f"{failed} download(s) failed; {len(leftovers)} external image link(s) still in {PAGE}.")
        print("Re-run the script, or download those images manually.")
        return 2
    print(f"All images are now local in ./{IMG_DIR}/ - commit that folder with {PAGE}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
