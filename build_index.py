#!/usr/bin/env python3
"""Rebuild search-index.json from the six searched pages.

Extraction rules (verified against the prior hand-built index):
  entry   <details class="tl-entry" id="..."> in each thread page
  fact    <div class="key-fact"> in each thread page (incl. voter-questions.html)
  howto   <div class="docs-callout"> in each page
  question <div class="va-item" id="..."> in voter-questions.html
"""
from bs4 import BeautifulSoup
import json, re

PAGES = [
    ("term-limits.html", "Term Limits", "\u29d6"),
    ("pension-record.html", "Pension Debt", "$"),
    ("leadership.html", "Leadership", "\u265b"),
    ("litigation.html", "Litigation", "\u2696"),
    ("transparency.html", "Transparency", "\u229e"),
    ("voter-questions.html", "Be Ready to Vote", "\u2713"),
]

def norm(text):
    return re.sub(r'\s+', ' ', text).strip()

def truncate(text, limit):
    text = norm(text)
    if len(text) <= limit:
        return text
    cut = text[:limit]
    if ' ' in cut:
        cut = cut.rsplit(' ', 1)[0]
    return cut + '\u2026'

def build():
    out = []
    for page, thread, icon in PAGES:
        with open(page, encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        # entries
        for d in soup.select('details.tl-entry[id]'):
            date = d.select_one('span.tl-date')
            teaser = d.select_one('span.tl-teaser')
            body = d.select_one('div.tl-body')
            out.append({
                "thread": thread, "icon": icon, "page": page,
                "anchor": d.get('id'),
                "title": norm(teaser.get_text(' ')) if teaser else '',
                "meta": norm(date.get_text(' ')) if date else '',
                "snippet": truncate(body.get_text(' ') if body else '', 180),
                "kind": "entry",
            })

        # facts
        for d in soup.select('div.key-fact'):
            full = norm(d.get_text(' '))
            out.append({
                "thread": thread, "icon": icon, "page": page,
                "anchor": "key-facts",
                "title": truncate(full, 90),
                "meta": "Key fact",
                "snippet": full,
                "kind": "fact",
            })

        # howto
        for d in soup.select('div.docs-callout'):
            h3 = d.select_one('h3')
            note = d.select_one('p.docs-note')
            out.append({
                "thread": thread, "icon": icon, "page": page,
                "anchor": None,
                "title": norm(h3.get_text(' ')) if h3 else '',
                "meta": "How to Vote",
                "snippet": norm(note.get_text(' ')) if note else '',
                "kind": "howto",
            })

        # questions (voter-questions.html only)
        if page == "voter-questions.html":
            for i, d in enumerate(soup.select('div.va-item[id]'), start=1):
                p = d.select_one('p')
                qnum = p.select_one('span.qnum')
                if qnum:
                    qnum.extract()
                box = p.select_one('span.box')
                if box:
                    box.extract()
                full = norm(p.get_text(' '))
                out.append({
                    "thread": thread, "icon": icon, "page": page,
                    "anchor": d.get('id'),
                    "title": truncate(full, 90),
                    "meta": "Question %02d" % i,
                    "snippet": full,
                    "kind": "question",
                })

    return out

if __name__ == "__main__":
    data = build()
    with open("search-index.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=True)
    print("Wrote", len(data), "entries")
