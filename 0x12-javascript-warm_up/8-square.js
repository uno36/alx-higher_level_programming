#!/usr/bin/node
/* a script that  prints a square */
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  let square = '';
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    } if (i < size - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
