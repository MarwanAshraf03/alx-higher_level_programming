#!/usr/bin/node
const request = require('request');
const filter = 18;
request("https://swapi-api.alx-tools.com/api/films/"+process.argv[2], function (error, response, body) {
  if (error) throw error;
  const b = JSON.parse(body);
  console.log(b)
    // for (let j = 0; j < b.results[i].characters.length; j++) {
    //   if (b.results[i].characters[j].includes(filter)) {
    //   }
    // }
});
