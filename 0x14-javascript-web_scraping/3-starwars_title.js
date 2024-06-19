#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) throw error;
  const b = JSON.parse(body);
  console.log(b.title);
});
