#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
  //If w/h are negtive or < 0. creates empty obj automatically
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
    }
  }
}

module.exports = Rectangle;
