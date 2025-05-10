// 시험 성적
// https://www.acmicpc.net/problem/9498

const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');
const inputVal = inputData[0].split(' ').map(Number);


function main(inputVal) {
  if (inputVal >= 90) console.log("A");
  else if (inputVal >= 80) console.log("B");
  else if (inputVal >= 70) console.log("C");
  else if (inputVal >= 60) console.log("D");
  else console.log("F");
}

main(inputVal);
