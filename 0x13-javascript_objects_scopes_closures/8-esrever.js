#!/usr/bin/node
/* returns the reversed version of a list */
exports.esrever = function (list) {
  let list1 = [];
  let j = list.length - 1;
  for (let i = 0; i < list.length; i++, j--) {
    list1[i] = list[j];
  }
  return list1;
};
