// Google Analytics 4 (same property/stream as russfeld.me; filter reports by hostname).
// Every archived page loads this file, so this is the only place the ID lives.
(function () {
  var id = 'G-HDHZ0ZXKQQ';
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', id);
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
  document.head.appendChild(s);
})();
