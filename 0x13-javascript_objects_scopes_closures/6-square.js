#!/usr/bin/node
const Square2 = require('./5-square');
class Square extends Square2 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let str1 = '';
      for (let i = 0; i < this.height; i++) {
        let str2 = '';
        for (let j = 0; j < this.width; j++) {
          str2 += c;
        }
        if (i === this.height - 1) {
          str1 += str2;
        } else {
          str1 += str2 + '\n';
        }
      }
      console.log(str1);
    }
  }
}
module.exports = Square;
