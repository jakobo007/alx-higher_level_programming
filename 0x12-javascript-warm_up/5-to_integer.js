#!/usr/bin/node
const args = process.argv.slice(2);
const[firstArg] = args;
const num = parseInt(firstArg);

if (isNaN(num)) {
    console.log("Not a number");
} else {
    console.log(`My number: ${num}`);
}

