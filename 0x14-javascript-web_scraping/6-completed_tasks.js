#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const b = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < b.length; i++) {
    if (!Object.keys(dict).includes('' + b[i].userId) && b[i].completed) {
      dict[b[i].userId] = 1;
    } else if (b[i].completed) {
      dict[b[i].userId] += 1;
    }
  }
  console.log(dict);
});
