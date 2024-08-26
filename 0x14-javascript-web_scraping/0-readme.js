#!/usr/bin/node

const fs = require('fs');
const FilePath = process.argv[2];

fs.readFile(FilePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
