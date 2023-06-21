#!/usr/bin/node
/* prints the number of movies where the
character “Wedge Antilles” is present. */
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (let result of body.results) {
      for (let character of result.characters) {
        if (character.endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
