/*-----------------------------------------------------
Sub  : [BOJ] 동전 0
Link : https://www.acmicpc.net/problem/11047
Level: 실버 4
Tag  : JS, 그리디
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


/* input */
const [N, K] = input[0].split(" ").map(Number);
const coins = input.slice(1, N + 1).map(Number).sort((a, b) => b - a);


/* solution */
let cnt = 0;
let rest = K;
let answer = 0;

for (let coin of coins) {
  cnt = parseInt(rest / coin)
  rest -= (coin * cnt)
  answer += cnt;
}


/* print */
console.log(answer);
