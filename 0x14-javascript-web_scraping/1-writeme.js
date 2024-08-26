#!/usr/bin/node

const fs = require('fs')
const FilePath = process.argv[2]
const String = process.argv[3]

fs.writeFile(FilePath, 'utf-8', (err) => {
    if (err) {
        console.log(err)
    }
});
