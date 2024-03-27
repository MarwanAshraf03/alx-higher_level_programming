#!/usr/bin/node
const request = require('request');
const filter = 18;
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const b = JSON.parse(body);
  let number = 0;
  for (let i = 0; i < b.count; i++) {
    for (let j = 0; j < b.results[i].characters.length; j++) {
      if (b.results[i].characters[j].includes(filter)) {
        number++;
      }
    }
  }
  console.log(number);
});
