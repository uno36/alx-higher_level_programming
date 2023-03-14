#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle */

class Rectangle {
  constructor (w, h) {
  // Method that initialize a instance
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
  // Method that prints the rectangle using the charactere 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
