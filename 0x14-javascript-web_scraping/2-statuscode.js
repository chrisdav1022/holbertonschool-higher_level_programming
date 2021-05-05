#!/usr/bin/node
/*
-The first argument is the URL to request
-The status code must be printed like
*/
const request = require('request');
const urlp = process.argv.slice(2, process.argv.length);
request
  .get(urlp[0])
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
