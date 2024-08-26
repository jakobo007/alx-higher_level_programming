#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const FilePath = process.argv[3];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(FilePath, body, 'utf-8', (err) => {
        if (err) {
            console.log(err);
        }
    });
  }
});
