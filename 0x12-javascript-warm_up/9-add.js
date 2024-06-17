#!/usr/bin/node
const args = process.argv.slice(2);
const [num1, num2] = args;

function add(a, b) {
    console.log(a + b);
}

add(parseInt(num1), parseInt(num2));
