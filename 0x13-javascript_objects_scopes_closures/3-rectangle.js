#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        //If w/h are negtive or < 0. creates empty obj automatically
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        //check if width and height are positive integers
        if (this.width && this.height) {
            for (let i = 0; i < this.height; i++) {
                console.log('X'.repeat(this.width));
            }
        }
    }
}

module.exports = Rectangle;

