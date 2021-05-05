#!/usr/bin/node
/*
-The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
-Only print users with completed task
*/
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  else {
    const d = {};
    for (const t of JSON.parse(body)) {
      if (t.completed) d[t.userId] ? d[t.userId]++ : d[t.userId] = 1;
    }
    console.log(d);
  }
});
