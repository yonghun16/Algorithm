// 구구단
// https://www.acmicpc.net/problem/2739

const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(inputData[0]);

for (let i=1; i<=9; i++) {
  console.log(`${n} * ${i} = ${n*i}`);
}
