#!/usr/bin/node
const dict = require('./101-data').dict;
const dict2 = dict.map(({key, value}) => {value, key});

console.log(dict);
console.log(dict2);
