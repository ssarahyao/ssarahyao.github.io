"""Pull Sarah's latest Stanford Daily articles into index.html.

Reads the public RSS feed of her author page and rewrites the block between
<!-- DAILY:START --> and <!-- DAILY:END --> in index.html.
Runs automatically every day via .github/workflows/update-daily.yml,
or by hand:  python3 scripts/update_daily.py
Uses only the Python standard library.
"""
import html
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED = "https://stanforddaily.com/author/sqyao/feed/"
INDEX = Path(__file__).resolve().parent.parent / "index.html"
MAX_ITEMS = 6


def fetch_items():
    req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0 (portfolio-feed-updater)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        root = ET.fromstring(r.read())
    items = []
    for it in root.iter("item"):
        desc = html.unescape(re.sub(r"<[^>]+>", "", it.findtext("description") or ""))
        desc = re.sub(r"\s*The post .* appeared first on The Stanford Daily\.?\s*$", "", desc, flags=re.S).strip()
        date = parsedate_to_datetime(it.findtext("pubDate"))
        items.append({
            "title": (it.findtext("title") or "").strip(),
            "link": (it.findtext("link") or "").strip(),
            "desc": desc,
            "date": date.strftime("%b %-d, %Y"),
        })
    return items[:MAX_ITEMS]


def render(items):
    out = []
    for i in items:
        e = lambda s: html.escape(s, quote=True)
        out.append(
            '          <article class="piece">\n'
            f'            <p class="piece-kicker">The Stanford Daily · {e(i["date"])}</p>\n'
            f'            <h4><a href="{e(i["link"])}" target="_blank" rel="noopener">{e(i["title"])}</a></h4>\n'
            f'            <p>{e(i["desc"])}</p>\n'
            '          </article>'
        )
    return "\n".join(out)


def main():
    items = fetch_items()
    if not items:
        print("Feed returned no articles; leaving index.html unchanged.")
        return 0
    page = INDEX.read_text(encoding="utf-8")
    new = re.sub(
        r"(<!-- DAILY:START -->\n).*?(\n\s*<!-- DAILY:END -->)",
        lambda m: m.group(1) + render(items) + m.group(2),
        page,
        flags=re.S,
    )
    if new == page:
        print("No new articles.")
    else:
        INDEX.write_text(new, encoding="utf-8")
        print(f"Updated with {len(items)} articles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
