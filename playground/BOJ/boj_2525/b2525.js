// 오븐 시계
// https://www.acmicpc.net/problem/2525

const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let a = Number(inputData[0].split(' ')[0]);
let b = Number(inputData[0].split(' ')[1]);
let c = Number(inputData[1].split(' ')[0]);


function main(a, b, c) {
  a += parseInt(c/60);
  b += c%60;
  if (b>=60) {
    a += 1;
    b -= 60;
  }
  if (a >= 24) {
    a %= 24; 
  }

  console.log(a, b);
}

main(a, b, c);
