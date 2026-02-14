// Research page — topic tag filtering
(function () {
  var buttons = document.querySelectorAll('.filter-btn');
  var cards = document.querySelectorAll('.card--project');
  if (!buttons.length || !cards.length) return;

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      // Update active state
      buttons.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');

      var topic = btn.getAttribute('data-topic');

      cards.forEach(function (card) {
        if (topic === 'all') {
          card.classList.remove('hidden');
        } else {
          var topics = card.getAttribute('data-topics') || '';
          if (topics.indexOf(topic) !== -1) {
            card.classList.remove('hidden');
          } else {
            card.classList.add('hidden');
          }
        }
      });
    });
  });
})();
