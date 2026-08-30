# The La Palma Record — Site Source

Complete source and configuration files for lapalmarecord.org, as of August 2026.

## Pages (12)
index.html, term-limits.html, pension-record.html, leadership.html,
litigation.html, transparency.html, voter-questions.html, depositions.html,
sources.html, about.html, contact.html, start-here.html

## Site-wide assets
- `style.css` — main stylesheet (typography, layout, color system, components)
- `nav-toggle.js` — mobile menu toggle + deep-link auto-expand for closed
  timeline entries (used when a link targets a `<details>` element's id,
  e.g. from a search result or the flow-of-funds anchor)

## Site search (added August 2026)
- `search-ui.css` — search overlay styling, loaded as its own stylesheet
  rather than merged into style.css
- `search.js` — search interaction logic (Fuse.js wiring, keyboard nav,
  result rendering, highlighting)
- `fuse.min.js` — Fuse.js v7.0.0, self-hosted rather than CDN-loaded
- `search-index.json` — the searchable content index

**Important:** `search-index.json` is a *generated* file, not hand-edited
source. It's built by a Python script (not included in this archive, but
available on request) that extracts timeline entries, key facts, and
voter-questions content from six pages: term-limits.html,
pension-record.html, leadership.html, litigation.html, transparency.html,
and voter-questions.html. Search is deliberately scoped to those six pages
only — Sources, About, Contact, Depositions, and Start Here are not indexed.

**Whenever those six pages are edited, `search-index.json` must be
regenerated** or search results will silently go stale (still findable,
just describing old content). Ask Claude to "rebuild the search index"
after a batch of content edits to those pages.

## SEO / crawl config
- `robots.txt`
- `sitemap.xml` — lists all 12 pages; not independently verified as live
  on the server as of this archive (see prior conversation notes)

## Deployment
All files are flat — no subfolders, no build step. Upload directly to the
GitHub Pages repository root. The 12 HTML pages reference style.css,
nav-toggle.js, search-ui.css, search.js, fuse.min.js, and
search-index.json by relative filename, so all files must be uploaded
together to the same directory.

## Not included in this archive
Image and PDF assets (photos, screenshots, campaign finance filings,
CalPERS reports, the flow-of-funds diagram, og-image.png, favicons, print
flyers, social graphics) are not included here, since they were originally
supplied by or generated separately from this HTML/CSS/JS source set.
