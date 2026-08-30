// Mobile nav toggle — expands/collapses the threadnav pill list behind a
// "Menu" button below the 640px breakpoint. No-op on desktop, where the
// list is always visible via CSS.
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.getElementById('navToggle');
    var nav = document.querySelector('nav.threadnav');
    if (!toggle || !nav) return;

    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });

    // Collapse the menu again once a link is tapped, so returning to a
    // page (e.g. via back button) doesn't leave it stuck open.
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  });
})();

// Deep-link auto-expand — if the page loads (or the hash changes) pointing
// at a <details> element's id, such as a #tl-... timeline entry linked
// from the master timeline page, open it and scroll it into view. Closed
// <details> elements are still focusable targets for a URL hash, but their
// body content stays hidden until opened — this makes the link actually
// land somewhere useful instead of just landing on the closed summary.
(function () {
  function openTargetFromHash() {
    var hash = window.location.hash;
    if (!hash || hash.length < 2) return;
    var target;
    try {
      target = document.querySelector(hash);
    } catch (e) {
      return;
    }
    if (!target) return;
    var details = target.closest ? target.closest('details') : null;
    if (details && !details.open) {
      details.open = true;
    }
    // Defer scroll slightly so the newly-revealed content has laid out.
    window.setTimeout(function () {
      target.scrollIntoView({ block: 'start' });
    }, 50);
  }

  document.addEventListener('DOMContentLoaded', openTargetFromHash);
  window.addEventListener('hashchange', openTargetFromHash);
})();
