#!/usr/bin/node
/*
-The first argument is the file path
-The second argument is the string to write
*/
const fs = require('fs');
const data = process.argv.slice(2, process.argv.length);

fs.writeFile(data[0], data[1], (err) => {
  if (err) { console.log(err); } else {
    fs.readFileSync(data[0], 'utf8');
  }
});
