/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 문제 제목
 * Link   : https://www.acmicpc.net/problem/1015
 * Level  : 실버 4
 * Tag    : JS, sorting
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

let input;

if (process.platform === "linux") {
  input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
} else {
  const path = require("path");
  const filePath = path.join(__dirname, "input.txt");
  input = require("fs").readFileSync(filePath, "utf-8").trim().split("\n");
}

const N = Number(input[0]);
const A = input[1].split(" ").map(Number);

// 1. (값, 원래 인덱스) 형태로 저장
const arr = A.map((value, index) => ({ value, index }));

// 2. 값 오름차순, 같으면 인덱스 오름차순
arr.sort((a, b) => {
  if (a.value !== b.value) return a.value - b.value;
  return a.index - b.index;
});

// 3. P 배열 생성
const P = Array(N);
for (let i = 0; i < N; i++) {
  P[arr[i].index] = i;
}

// 4. 출력
console.log(P.join(" "));
