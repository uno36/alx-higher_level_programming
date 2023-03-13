#!/usr/bin/node
/* a script that computes and prints a factorial
*/
function factorial (a) {
  if (isNaN(a)) {
    return (1);
  } else if (a === 1) {
    return (1);
  } else {
    return (factorial(a - 1) * a);
  }
}
console.log(factorial(process.argv[2]));
