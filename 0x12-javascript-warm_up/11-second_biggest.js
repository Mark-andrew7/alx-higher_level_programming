#!/usr/bin/node

function secondBiggest (...args) {
  if (args.length <= 1) {
    console.log(0);
  } else {
    const sortArgs = args.map(Number).sort((x, y) => y - x);
    return sortArgs[1];
  }
}

const arg = process.argv.slice(2);
console.log(secondBiggest(...arg));
