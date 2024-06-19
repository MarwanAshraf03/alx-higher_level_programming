#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const firstVar = parseInt(process.argv[2]);
const secondVar = parseInt(process.argv[3]);
console.log(add(firstVar, secondVar));
