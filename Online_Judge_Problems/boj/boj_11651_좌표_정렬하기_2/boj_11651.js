/*-----------------------------------------------------
Sub  : [BOJ] 좌표 정렬하기 2
Link : https://www.acmicpc.net/problem/11651
Level: 실버 5
Tag  : JS, Sort
Memo
-----------------------------------------------------*/

const TEST_MODE = false;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// input
const N = Number(input[0]);
const arr = input.slice(1, N + 1).map((el) => el.split(' ').map(Number));


// sort
arr.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
})

// print
let answer = "";
for (let point of data) {
  answer += print[0] + " " + point[1] + "\n";
}

console.log(answer);
