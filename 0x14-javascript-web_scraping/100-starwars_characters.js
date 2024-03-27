#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) throw error;
  const b = JSON.parse(body);
  for (let j = 0; j < b.characters.length; j++) {
    request(b.characters[j], function (error, response, bb) {
      if (error) throw error;
      console.log(JSON.parse(bb).name);
    });
  }
});
