<<<<<<< HEAD
const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
})
=======
// 입력 받기 (Node.js 환경에서는 'fs' 모듈을 사용해서 입력을 받을 수 있음)
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// N과 M을 가져오기
const [N, M] = input[0].split(" ").map(Number);
>>>>>>> d88c5d3c6699e899a71452e70188d2096479a5ff

// 행렬 A와 B 가져오기
let A = [];
let B = [];

<<<<<<< HEAD
rl.on('line', (line) => {
  data.push(line.trim())
}).on('close', () => {
  const [n, m] = data[0].split(' ').map(Number)
  console.log(n)
});
=======
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
>>>>>>> d88c5d3c6699e899a71452e70188d2096479a5ff
