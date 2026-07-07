/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] BABBA
 * Link   : https://www.acmicpc.net/problem/9625
 * Level  : 실버 5
 * Tag    : JS, DP
 * Memo
 * -----------------------------------------------------------
 */

// [환경 설정]
const TEST_MODE = false;
let input;

// [입력 처리]
if (TEST_MODE) {
  // 로컬 테스트 (input.txt 파일 읽기)
  const filePath = require("path").join(__dirname, "input.txt");
  input = require("fs").readFileSync(filePath, "utf-8").trim().split("\n");
} else {
  // 제출 환경 (표준 입력)
  input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
}

const K = Number(input);

if (K === 0) {
  // 문제에서 K >= 1 이지만 안전하게 처리
  console.log("1 0");
  process.exit(0);
}

let a = 0; // F(0)
let b = 1; // F(1)

for (let i = 2; i <= K; i++) {
  const next = a + b; // F(i) = F(i-2) + F(i-1)
  a = b;
  b = next;
}

// after loop:
// if K == 1 -> a=0 (F0), b=1 (F1)
// in general: A = F(K-1), B = F(K)
if (K === 1) {
  console.log(`${0} ${1}`);
} else {
  // now a = F(K-1), b = F(K)
  console.log(`${a} ${b}`);
}
