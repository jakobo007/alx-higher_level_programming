#!/usr/bin/node
function factorial(n) {
    if (isNaN(n) || n === 0) {
        console.log(1);
    }
    if (n < 0) {
        console(1);
    }
    console.log(n === 1 ? 1 : n * factorial(n - 1));
}
