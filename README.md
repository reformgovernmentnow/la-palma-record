# The La Palma Record — Site Package
LPR-Package-20260902-0804

Complete source and configuration files for lapalmarecord.org, as of this
export (September 2, 2026).

## Pages (13)
index.html, term-limits.html, pension-record.html, leadership.html,
litigation.html, transparency.html, voter-questions.html, depositions.html,
sources.html, about.html, contact.html, start-here.html, timeline.html

timeline.html is the master timeline — every dated event across the five
investigative threads, in one chronological view. It is intentionally not
in the site's main nav (reachable via a homepage callout instead).

## Site-wide assets
- style.css — main stylesheet
- nav-toggle.js — mobile menu toggle + deep-link auto-expand for closed
  timeline entries (used by search results and the master timeline's
  "Read the full record" links)

## Site search
- search-ui.css — search overlay styling
- search.js — search interaction logic (Fuse.js wiring, keyboard nav,
  result rendering, highlighting)
- fuse.min.js — Fuse.js v7.0.0, self-hosted rather than CDN-loaded
- search-index.json — the searchable content index

**Important:** search-index.json is a *generated* file. It's built by a
Python script (not included here, available on request) that extracts
timeline entries, key facts, and voter-questions content from six pages:
term-limits.html, pension-record.html, leadership.html, litigation.html,
transparency.html, and voter-questions.html. Search is deliberately scoped
to those six pages only.

Whenever those six pages are edited, search-index.json must be
regenerated or search results will describe stale content. Ask Claude to
"rebuild the search index" after a batch of content edits.

**timeline.html has a related manual-sync requirement**: several of its
entries mirror teaser text pulled directly from the five thread pages.
If a thread page's timeline-entry teaser changes, the matching line on
timeline.html needs to be updated by hand to stay in sync — this is not
automated.

## SEO / crawl config
- robots.txt
- sitemap.xml — lists site pages; verify independently that this is
  actually deployed and current, since it is not auto-regenerated when
  new pages (like timeline.html) are added.

## Deployment
All files are flat — no subfolders, no build step. Upload directly to
the GitHub Pages repository root. All 13 HTML pages reference style.css,
nav-toggle.js, search-ui.css, search.js, fuse.min.js, and
search-index.json by relative filename, so all files should be uploaded
together to the same directory.

## Not included in this package
Image and PDF assets (photos, screenshots, campaign finance filings,
CalPERS reports, the flow-of-funds diagram, og-image.png, favicons, print
flyers, social graphics) are not included, since they were originally
supplied by or generated separately from this HTML/CSS/JS source set and
are not stored in this working environment.
