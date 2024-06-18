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

    rotate() {
        //exchanges the width and height of rectangle
        if (this.width && this.height) {
		const temp = this.width;
		this.width = this.height;
		this.height = temp;
	}
    }
    
    double() {
        //multiplies the width and height by 2
        if (this.width && this.height) {
		this.width *= 2;
		this.height *= 2;
	}
    }
}

module.exports = Rectangle;

