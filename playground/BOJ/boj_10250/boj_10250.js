/*
----------------------------------------------
Sub : [BOJ] ACM호텔
Link: https://www.acmicpc.net/problem/10250
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);

const sol = (H, W, N) => {
  let number = 1;
  for (let i = 0; i < W; i++) {
    for (let j = 0; j < H; j++) {
      if (number === N) {
        console.log((j + 1) * 100 + (i + 1));
        return;
      }
      number += 1;
    }
  }
};

for (let i = 1; i <= T; i++) {
  let [H, W, N] = input[i].split(" ").map(Number);
  sol(H, W, N);
}
