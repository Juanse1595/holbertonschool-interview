#!/usr/bin/node
const request = require('request');

if (!process.argv[2]) {
  console.log('Usage: ./0-starwars_characters.js movieId');
  process.exit(1);
}

let characters = false;
request('https://swapi-api.hbtn.io/api/films', async (error, response, body) => {
  error && console.error('Error: ', error);
  body = JSON.parse(body);
  const movieId = process.argv[2];
  const results = body.results;
  for (const movie of results) {
    if (movie.episode_id === movieId) { characters = movie.characters; }
  }
  if (characters) {
    for (const char of characters) {
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
  }
});
