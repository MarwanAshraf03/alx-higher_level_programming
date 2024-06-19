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

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
