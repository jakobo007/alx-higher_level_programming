#!/usr/bin/node
function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
	return n * factorial(n - 1);
  }
<<<<<<< HEAD
=======
    if (isNaN(n) || n === 0) {
        console.log(1);
    }
    if (n < 0) {
        console(1);
    }
    console.log(n === 1 ? 1 : n * factorial(n - 1));
>>>>>>> 77122fb30150f1ab909a06ecc2be8504fd53883d
}
const args = process.argv.slice(2);
const n = parseInt(args, 10);
console.log(factorial(n));
