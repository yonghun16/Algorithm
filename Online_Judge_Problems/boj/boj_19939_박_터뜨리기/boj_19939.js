/*-----------------------------------------------------
Sub  : [BOJ] 박 터뜨리기
Link : https://www.acmicpc.net/problem/19939
Level: 실버 4
Tag  : JS, greedy
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input2.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}

// input
const [n, k] = input[0].split(' ').map(Number);

// 최소 합 계산: 1 + 2 + ... + k
const sum = ((1 + k) * k) / 2;

// 남은 공을 k로 나눈 나머지
let c = (n - sum) % k;

// 나머지에 따른 차이 계산
if (c === 0) {
  c = k - 1;
} else {
  c = k;
}

// 공이 부족한 경우
if (n < sum) {
  console.log(-1);
} else {
  console.log(c);
}
