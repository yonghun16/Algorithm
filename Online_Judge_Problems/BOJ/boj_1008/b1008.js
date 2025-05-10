// https://www.acmicpc.net/problem/1008

let fs = require('fs');
let inputData = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputVal = inputData[0].split(' ');

const a = parseInt(inputVal[0]);
const b = parseInt(inputVal[1]);

console.log(a / b);

