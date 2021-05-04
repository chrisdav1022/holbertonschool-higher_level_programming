#!/usr/bin/node

/*
- The content of the file must be read in utf-8
-If an error occurred during the reading, print the error object
*/

const files = process.argv.slice(2, process.argv.length);
const fs = require('fs');
files.forEach(element => {
  fs.readFile(element, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString());
    }
  });
});