#!/usr/bin/node
// defines function that returns a reversed array
exports.esrever = function(list) {
  var reversed = [];
  for (var i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};