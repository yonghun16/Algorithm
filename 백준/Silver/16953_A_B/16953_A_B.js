/*-----------------------------------------------------
Sub  : [BOJ] A->B
Link : https://www.acmicpc.net/problem/16953
Level: 실버 2
Tag  : JS, greedy, DFS
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

const [A, B] = input[0].split(' ').map(Number);

// 재귀 함수
function dfs(current, target, steps) {
  if (current > target) return -1;
  if (current === target) return steps;

  const next1 = dfs(current * 2, target, steps + 1);
  const next2 = dfs(current * 10 + 1, target, steps + 1);

  if (next1 === -1 && next2 === -1) return -1;
  else if (next1 === -1) return next2;
  else if (next2 === -1) return next1;
  else return Math.min(next1, next2);
}

const result = dfs(A, B, 1);
console.log(result);
