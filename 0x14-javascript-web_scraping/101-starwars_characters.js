#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const charachters = data.charachters;

    request(characters, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        const cast = JSON.parse(body);
        console.log(cast.name);
      }
    })
  }
});