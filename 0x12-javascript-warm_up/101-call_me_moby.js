#!/usr/bin/node
function fnCall (x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}
