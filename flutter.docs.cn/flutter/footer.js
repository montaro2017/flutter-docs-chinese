(function() {
  var span = document.querySelector('footer>span');
  if (span) {
    span.innerText = 'Flutter 3.49.0-1.0.pre-91 • 2026-10-08 10:00 • abaf9c5237 • stable';
  }
  var sourceLink = document.querySelector('a.source-link');
  if (sourceLink) {
    sourceLink.href = sourceLink.href.replace('/main/', '/abaf9c5237/');
  }
})();
