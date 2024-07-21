// A + B
// https://www.acmicpc.net/problem/1000

let fs = require('fs');
let inputData = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputNum = inputData[0].split(' ').map(Number);

const a = inputNum[0];
const b = inputNum[1];

function getSum(a, b) {
  return a + b
}

console.log(getSum(a, b));
