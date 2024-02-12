#!/usr/bin/node
function factorial (a) {
  if (!a) {
    return (1);
  }
  if (a === 0) {
    return (1);
  }
  return (factorial(a - 1) * a);
}
console.log(factorial(parseInt(process.argv[2])));
