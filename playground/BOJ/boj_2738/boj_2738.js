/* ----------------------------------------------
Sub: [BOJ] 2738. 행렬 덧셈
Link: https://www.acmicpc.net/problem/2738
Tag: js, 2차원 배열
Memo
---------------------------------------------- */

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);

// 행렬 A와 B 가져오기
let A = [];
let B = [];

for (let i = 1; i <= N; i++) {
  A.push(input[i].split(" ").map(Number));
}

for (let i = N + 1; i <= 2 * N; i++) {
  B.push(input[i].split(" ").map(Number));
}

// 결과 행렬 계산
let result = Array.from(Array(N), () => new Array(M));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    result[i][j] = A[i][j] + B[i][j];
  }
}

// 결과 출력
result.forEach((row) => console.log(row.join(" ")));
