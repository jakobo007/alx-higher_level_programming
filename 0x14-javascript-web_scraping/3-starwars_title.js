#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const API = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(API, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
