#!/usr/bin/node
/* a class Square that defines a square and inherits
from Rectangle of 4-rectangle.js */
const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
