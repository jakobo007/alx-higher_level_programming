#!/usr/bin/node
const args = process.argv.slice(2);
const [x] = args;
const myVar = "C is fun";


if (isNaN(parseInt(x))) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < x; i++) {
        console.log(myVar);
    }
}

