/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 2xn 타일링
 * Link   : https://www.acmicpc.net/problem/11726
 * Level  : Silver 3
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

const n = parseInt(input, 10);
const MOD = 10007;

if (n === 1) {
  console.log(1);
  process.exit(0);
}

let prev2 = 1; // dp[1]
let prev1 = 2; // dp[2]
let current = 0;

for (let i = 3; i <= n; i++) {
  current = (prev1 + prev2) % MOD;
  prev2 = prev1;
  prev1 = current;
}

console.log(n === 2 ? prev1 : current);
