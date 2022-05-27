#!/usr/bin/node
const request = require('request');

if (!process.argv[2])
{
    console.log('Usage: ./0-starwars_characters.js movie_id')
    process.exit(1);
}

let characters = false;
request('https://swapi-api.hbtn.io/api/films', (error, response, body) => {
    body = JSON.parse(body);
    movie_id = process.argv[2];
    results = body.results;
    for (const movie of results) {
        if (movie.episode_id == movie_id) {
            characters = movie.characters;
        }
    }
    if (characters) {
        for (const char of characters) {
            request(char, (error, response, body) => {
                console.log(JSON.parse(body).name);
            })
        }
    }
})
