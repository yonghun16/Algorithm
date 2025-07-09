/*-----------------------------------------------------
Sub  : [BOJ] A->B
Link : https://www.acmicpc.net/problem/16953
Level: 실버 2
Tag  : JS, 그리디
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input1.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
} else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}

// input
let [A, B] = input[0].split(' ').map(Number);

// solution
let count = 1;
while (B !== A) {
  if (B < A) {
    count = -1;
    break;
  }

  if (B % 10 === 1) {
    B = Math.floor(B / 10);
  } else if (B % 2 === 0) {
    B = B / 2;
  } else {
    count = -1;
    break;
  }
  count++;
}

// output
console.log(count);
