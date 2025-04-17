/*
----------------------------------------------
Sub : [BOJ] 별찍기-2
Link: https://www.acmicpc.net/problem/2439
Tag : JS
Memo
----------------------------------------------
*/

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

N = Number(input[0])

for (let i=0; i<N; i++) {
  console.log(' '.repeat(N-i-1) + '*'.repeat(i+1));
}
