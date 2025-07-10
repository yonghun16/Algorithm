/*-----------------------------------------------------
Sub  : [BOJ] 수들의 합
Link : https://www.acmicpc.net/problem/1789
Level: 실버 5
Tag  : JS, greedy
Memo
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input1.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
}
else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}


// input
S = Number(input[0]);

// solution
let acc = 0
let count = 0

for (let i = 1; i < S+1; i++) {
  acc += i
  count += 1
  if (acc > S) {
    count -= 1
    break
  }
}

// output
console.log(count);
