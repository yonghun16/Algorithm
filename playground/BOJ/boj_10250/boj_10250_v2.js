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

for (let i = 1; i <= T; i++) {
  const [H, W, N] = input[i].split(" ").map(Number);

  // N번째 손님이 배정될 층 계산
  const floor = N % H === 0 ? H : N % H;

  // N번째 손님이 배정될 방 번호 계산
  const roomNumber = Math.ceil(N / H);

  // 방 번호는 YYXX 형태
  console.log(`${floor}${roomNumber < 10 ? '0' : ''}${roomNumber}`);
}
