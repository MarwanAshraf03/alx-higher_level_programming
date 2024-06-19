#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], (err, file) => {
  if (err) throw err;
  console.log(file.toString());
});
