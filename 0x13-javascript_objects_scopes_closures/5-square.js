#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor(size) {
	//super takes both width and height
        super(size, size);
        this.size = size;
    }
}

module.exports = Square;
