#!/usr/bin/node
const arr = [];
if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  console.log(arr.sort((a, b) => a - b)[arr.length - 2]);
}
