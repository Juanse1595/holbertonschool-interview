#!/usr/bin/node
const request = require('request');

if (!process.argv[2]) {
  console.log('Usage: ./0-starwars_characters.js movieId');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`
request(url, async (error, response, body) => {
  error && console.error('Error: ', error);
  body = JSON.parse(body);
  for (const char of body.characters) {
    await new Promise ((resolve, reject) => {
      request(char, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      })
    })
  }
});
