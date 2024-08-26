#!/usr/bin/node

import request from 'request';
const MovieID = process.argv[2];
const URL = "https://swapi-api.alx-tools.com/";

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data =JSON.parse(body);
    const characters = data.characters;

    characters.forEach(character => {
        request(`${URL}/${MovieID}`, (error, response, body) => {
            if (error) {
                console.log(error);
            } else {
                const cast = JSON.parse(body);
                console.log(cast.name);
            }
        });
    });
  }
});
