#!/usr/bin/node
/* prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
if (!process.argv[2]) {
  console.log('No argument');
} else if (parseInt(process.argv[2])) {
  console.log('My number:', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
