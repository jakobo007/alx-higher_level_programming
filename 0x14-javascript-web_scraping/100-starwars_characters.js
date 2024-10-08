#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    const species = data.species;
    const vehicles = data.vehicles;

    characters.forEach(character => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });

    vehicles.forEach(vehicle => {
      request(vehicle, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const vehicleData = JSON.parse(body);
          console.log(vehicleData.name);
        }
      })
    });

    species.forEach(specie => {
    request(specie, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        const specieData = JSON.parse(body);
        console.log(specieData.name);
      }
    })
    });
  }
});
