#!/usr/bin/node
function factorial(n) {
<<<<<<< HEAD
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
	return n * factorial(n - 1);
  }
=======
    if (isNaN(n) || n === 0) {
        console.log(1);
    }
    if (n < 0) {
        console(1);
    }
    console.log(n === 1 ? 1 : n * factorial(n - 1));
>>>>>>> b876e16d73248390c86a7042888af4addd688598
}

const args = process.argv.slice(2);
const n = parseInt(args, 10);
console.log(factorial(n));
