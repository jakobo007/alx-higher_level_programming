#!/usr/bin/node
const Square = require('./5-square');
class Square extends Square {
    //prints rectangle using character c
    charPrint(c) {
        if (c === undefined) {
            c = "X"
        }
        
        for (let i = 0; i < size; i++) {
            console.log(c.repeat(this.size));
        }
    }
}

//module.exports = Square;
