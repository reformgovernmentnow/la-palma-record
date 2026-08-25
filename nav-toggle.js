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
