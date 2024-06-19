#!/usr/bin/node
function factorial(n) {
    if (isNaN(n) || n === 0) {
        return 1;
    }

    if (n < 0) {
        return 1;
    }

    return n === 1 ? 1 : n * factorial(n - 1);
}
