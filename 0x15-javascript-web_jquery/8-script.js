$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  for (let result of data.results) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  }
});
