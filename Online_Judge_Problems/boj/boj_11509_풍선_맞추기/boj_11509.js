/*-----------------------------------------------------
Sub  : [BOJ] 풍선 맞추기
Link : https://www.acmicpc.net/problem/11509
Level: 골드 5
Tag  : JS, greedy
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


// input
const N = Number(input[0]);
const balloons = input[1].trim().split(' ').map(Number);
const arrowHeight = new Array(1000000).fill(0);
let answer = 0;

// processing
for (ball of balloons) {
  if (arrowHeight[ball] > 0) {
    arrowHeight[ball] -= 1;
    arrowHeight[ball - 1] += 1;
  } else {
    arrowHeight[ball - 1] += 1;
    answer += 1;
  }
}

// output
console.log(answer)
