#!/usr/bin/node
const noOcc = parseInt(process.argv[2]);
if (!noOcc) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < noOcc; i++) {
  console.log('C is fun');
}
