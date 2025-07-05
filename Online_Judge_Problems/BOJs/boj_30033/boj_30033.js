/*
----------------------------------------------
Sub : [BOJ] Rust Study
Link: https://www.acmicpc.net/problem/30033
Tag : JS, 
Memo
----------------------------------------------
*/

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 데이터 처리
const N = parseInt(input[0]); // 일수 N
const A = input[1].split(' ').map(Number); // 계획한 페이지 수 A
const B = input[2].split(' ').map(Number); // 실제 공부한 페이지 수 B

let count = 0;
for (let i = 0; i < N; i++) {
  if (B[i] >= A[i]) {
    count++;
  }
}

// 결과 출력
console.log(count);
