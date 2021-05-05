#!/usr/bin/node
/*
-The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
-Only print users with completed task
*/
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body);
    const objeto = {};
    for (let i = 0; i < results.length; i++) {
      if (objeto[results[i].userId] === undefined) {
        objeto[results[i].userId] = 1;
      } else if (results[i].completed === true) {
        objeto[results[i].userId] += 1;
      }
    }
    console.log(objeto);
  }
});
