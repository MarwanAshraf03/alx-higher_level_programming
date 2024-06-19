#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
} else {
  let str1 = '';
  let str2 = '';
  for (let i = 0; i < size; i++) {
    str2 = '';
    for (let j = 0; j < size; j++) {
      str2 = str2 + 'X';
    }
    if (i !== size - 1) {
      str1 = str1 + str2 + '\n';
    } else {
      str1 = str1 + str2;
    }
  }
  console.log(str1);
}
