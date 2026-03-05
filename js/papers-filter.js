// Papers page — conference filter (round buttons)
(function () {
  var bar = document.querySelector('.papers-filter-bar');
  if (!bar) return;
  var buttons = bar.querySelectorAll('.filter-btn');
  var sections = document.querySelectorAll('.papers-section');
  if (!buttons.length || !sections.length) return;

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var conference = btn.getAttribute('data-conference');
      sections.forEach(function (section) {
        if (conference === 'all') {
          section.classList.remove('hidden');
        } else {
          if (section.getAttribute('data-conference') === conference) {
            section.classList.remove('hidden');
          } else {
            section.classList.add('hidden');
          }
        }
      });
    });
  });
})();
