#!/usr/bin/node

const Request = require('request');
const URL = process.argv[2];

Request(URL, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
