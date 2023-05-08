$.getJSON('https://fourtonfish.com/hellosalut/?lang=' + document.documentElement.lang, function (data) {
  $('DIV#hello').text(data.hello);
});
