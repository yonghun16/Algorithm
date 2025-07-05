// 긴자리 계산
// https://www.acmicpc.net/problem/2338

const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const A = BigInt(input[0]);
const B = BigInt(input[1]);

const sum = A + B;
const difference = A - B;
const product = A * B;

console.log(sum.toString());
console.log(difference.toString());
console.log(product.toString());
