#!/usr/bin/node
if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  console.log(process.argv.sort()[process.argv.length - 2]);
}
