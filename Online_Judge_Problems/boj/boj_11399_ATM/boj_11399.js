/*-----------------------------------------------------
Sub  : [BOJ] ATM
Link : https://www.acmicpc.net/problem/11399
Level: 실버 4
Tag  : JS, 그리디
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


/* input */
const N = Number(input[0]);
const waiters = input[1].split(" ").map(Number).sort((a, b) => a - b);


/* solve */
let total = 0;
let acc = 0;

for (let i = 0; i < N; i++) {
  acc += waiters[i];
  total += acc;
}


/* output */
console.log(total);
