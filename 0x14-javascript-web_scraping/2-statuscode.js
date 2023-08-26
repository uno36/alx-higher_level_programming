#!/usr/bin/node
/* display the status code of a GET request. */
const request = require('request');
const url = process.argv[2];
request(url, function (error, data) {
  if (error) {
    console.log('code:', error);
  } else {
    console.log('code:', data.statusCode);
  }
});
