#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const b = JSON.parse(body);
  let number = 0;
  for (let i = 0; i < b.count; i++) {
    if (b.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      number++;
    }
  }
  console.log(number);
});
