#!/usr/bin/node
function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
	return n * factorial(n - 1);
  }
}

const args = process.argv.slice(2);
const n = parseInt(args, 10);
console.log(factorial(n));
