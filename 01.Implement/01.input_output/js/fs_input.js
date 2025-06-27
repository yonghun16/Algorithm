/*
----------------------------------------------
Sub: 행렬 덧셈
Tag: js
Memo : 입력 받기 (Node.js 환경에서는 'fs' 모듈을 사용해서 입력을 받을 수 있음)
  const fs = require('fs')
  const inputData = fs.readFileSync('/dev/stdin').toString().split('\n')
  const inputVal = inputData[0].split(' ').map(Number)

  console.log(inputVal)
----------------------------------------------
*/
const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');


// N과 M을 가져오기
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
