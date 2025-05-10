/*-----------------------------------------------------
Sub  : [BOJ] 완전 제곱수
Link : https://www.acmicpc.net/problem/6131
Level: 브론즈 3
Tag  : JS, Brute Force
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const MAX = 500;
let [a, b, count] = [1, 1, 0];

// 입력
const n = Number(input[0]);

while (b < MAX) {
  if (a ** 2 === b ** 2 + n) {
    count++;
    b++;
    a = b;
  }
  if (a ** 2 > b ** 2 + n) {
    b++;
    a = b;
    continue;
  }
  a++;
}

// 출력
console.log(count);
