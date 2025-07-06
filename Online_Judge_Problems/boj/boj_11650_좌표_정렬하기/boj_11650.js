/*-----------------------------------------------------
Sub  : [BOJ] 좌표 정렬하기
Link : https://www.acmicpc.net/problem/11650
Level: 실버 5
Tag  : JS, Sort
Memo
-----------------------------------------------------*/

const TEST_MODE = true;   // True -> file input, False -> stdin input

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input2.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// 입력
const N = Number(input[0]);
const arr = input.slice(1, N + 1).map((el) => el.split(' ').map(Number));

// 정렬
arr.sort((a, b) => {
  if (a[0] === b[0]) return a[1] - b[1];
  return a[0] - b[0];
});

// 출력
arr.forEach(el => {
  console.log(...el);
});
