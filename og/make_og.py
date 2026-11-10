#!/usr/bin/env python3
"""Render a 1200x630 Open Graph share image for each partner.

Writes og/<SLUG>-og.png. Needs Playwright:  pip install playwright && playwright install chromium
Run from the repo root:  python3 og/make_og.py
"""
import html
import json
import pathlib

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1200px;height:630px;background:#102a42;color:#f6f4ef;font-family:Inter,sans-serif;position:relative;overflow:hidden}}
.wrap{{position:absolute;inset:0;padding:72px 80px;display:flex;flex-direction:column}}
.eyebrow{{font-weight:600;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:#e9a25b}}
h1{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:82px;line-height:1.02;margin-top:28px;max-width:900px}}
.foot{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between}}
.brand{{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:30px}}
.brand span{{color:#e9a25b}}
.pill{{background:#e9a25b;color:#102a42;font-weight:600;font-size:26px;padding:16px 28px;border-radius:10px}}
.bar{{position:absolute;right:0;top:0;bottom:0;width:18px;background:#e9a25b}}
</style></head><body>
<div class="bar"></div>
<div class="wrap">
  <p class="eyebrow">Give back. Grow your business.</p>
  <h1>Give $5 to {partner}. Get a free SEO audit.</h1>
  <div class="foot">
    <p class="brand">My Launch Partner <span>×</span> {partner}</p>
    <p class="pill">100% goes to {partner}</p>
  </div>
</div>
</body></html>"""


def main():
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for f in sorted((ROOT / "partners").glob("*.json")):
            p = json.loads(f.read_text())
            pg = b.new_page(viewport={"width": 1200, "height": 630})
            pg.set_content(PAGE.format(partner=html.escape(p["partner"])))
            pg.wait_for_timeout(1500)
            out = ROOT / "og" / f"{p['slug']}-og.png"
            pg.screenshot(path=str(out))
            print("wrote", out.relative_to(ROOT))
        b.close()


if __name__ == "__main__":
    main()
