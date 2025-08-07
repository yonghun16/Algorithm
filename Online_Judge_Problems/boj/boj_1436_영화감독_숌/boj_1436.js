/*-----------------------------------------------------
Sub  : [BOJ] 영화감독 숌
Link : https://www.acmicpc.net/problem/1436
Level: 실버 5
Tag  : JS, brute force
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
const N = Number(input);

let count = 0;
let num = 665;

while (true) {
  num++;
  if (String(num).includes('666')) {
    count++;
    if (count === N) {
      console.log(num);
      break;
    }
  }
}
