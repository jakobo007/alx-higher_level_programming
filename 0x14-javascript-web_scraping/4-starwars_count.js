#!/usr/bin/node

const request = require('request');
const charID = 18;
const URL = process.argv[2]

request(URL, (err, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
        if (film.characters.includes(`${URL}/${charID}/`)) {
            count++;
        }
    });
    console.log(count);
  }
});
