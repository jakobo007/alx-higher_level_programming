#!/usr/bin/node
//prints a list in reverse
exports.esrever = function (list) {
    let newList = [];
    for (let i = list.length - 1; i >= 0; i--) {
        newList.push(list[i]);
    }
    return newList;
}
