#!/usr/bin/node
/* computes the number of tasks completed by user id. */
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let completed = {};
    for (let todo of body) {
      if (todo.completed === true) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 0;
        }
        completed[todo.userId]++;
      }
    }
    console.log(completed);
  }
});
