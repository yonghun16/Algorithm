/*-----------------------------------------------------
Sub  : [BOJ] 소트인사이드
Link : https://www.acmicpc.net/problem/1427
Level: 실버 5
Tag  : JS, 정렬, 문자열
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input3.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// input
const number = input[0];

// solution
let arr = [];
for (el of number) {
  arr.push(Number(el));
}
arr.sort((a, b)=> b-a)


// print
let answer = '';
for (el of arr) {
  answer += el
}
console.log(answer);
