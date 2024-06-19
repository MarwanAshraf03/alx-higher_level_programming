#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str1 = '';
    for (let i = 0; i < this.height; i++) {
      let str2 = '';
      for (let j = 0; j < this.width; j++) {
        str2 += 'X';
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

module.exports = Rectangle;
