#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  const str1 = counter + ': ' + item;
  console.log(str1);
  counter++;
};
