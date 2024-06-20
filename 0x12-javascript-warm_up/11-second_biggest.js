#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));
if (args.length <= 1) {
    console.log(0);
} else {
    const argsSort = [...new Set(args)].sort((a, b) => b - a);

    console.log(argsSort[1]);
}
