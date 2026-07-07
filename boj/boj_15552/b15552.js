// 빠른 A+B
// https://www.acmicpc.net/problem/15552

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let testCaseCount = Number(input[0]);
let result = '';

for (let i=1; i<=testCaseCount; i++) {
  let caseData = input[i].split(' ');
  let firstNumberOfCaseData = Number(caseData[0]);
  let secondNumberOfCaseData = Number(caseData[1]);
  result += (firstNumberOfCaseData + secondNumberOfCaseData) + '\n';
}

console.log(result);
