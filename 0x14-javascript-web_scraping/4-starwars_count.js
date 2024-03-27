#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const b = JSON.parse(body);
  let number = 0;
  for (let i = 0; i < b.count; i++) {
    for (let j = 0; j < b.results[i].characters.length; j++) {
      if (b.results[i].characters[j].includes('/18/')) {
        number++;
      }
    }
  }
  console.log(number);
});
