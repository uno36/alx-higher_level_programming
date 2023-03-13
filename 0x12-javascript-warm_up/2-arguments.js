#!/usr/bin/node
/* prints a message depending of the number of arguments passed */
if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
