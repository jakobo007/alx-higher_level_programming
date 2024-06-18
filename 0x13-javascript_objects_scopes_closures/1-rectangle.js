#!/usr/bin/node
class Rectangle {
    constructor(name) {
        this.name = name;
    }
    constructor(w, h) {
        this.height = h;
        this.width = w;
    }
}
module.exports = Rectangle;
