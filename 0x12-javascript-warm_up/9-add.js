#!/usr/bin/node
function add (num1, num2) {
  const sum = num1 + num2;
  console.log(sum);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
