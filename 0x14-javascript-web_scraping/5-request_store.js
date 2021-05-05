#!/usr/bin/node
/*
-The first argument is the URL to request
-The second argument the file path to store
*/
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, reponse, body) {
  if (!error) {
    const datos = body;
    fs.writeFile(process.argv[3], datos, () => {
      const redirect = `datos > ${process.argv[3]}`;
      return redirect;
    });
  }
});
