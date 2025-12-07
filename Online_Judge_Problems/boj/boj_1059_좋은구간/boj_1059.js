/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 좋은 구간
 * Link   : https://www.acmicpc.net/problem/1059
 * Level  : 실버 4
 * Tag    : JS, Math
 * Memo
 * -----------------------------------------------------------
 */

const TEST_MODE = true;
let input;

if (TEST_MODE) {
  const filePath = require("path").join(__dirname, "input.txt");
  input = require("fs").readFileSync(filePath, "utf-8").trim().split("\n");
} else {
  input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
}

let idx = 0;
const L = Number(input[idx++]);
let S = input[idx++].split(" ").map(Number); // 한 줄에서 S 읽기
const n = Number(input[idx++]);

S.sort((a, b) => a - b);

if (S.includes(n)) {
  console.log(0);
  process.exit(0);
}

let Lb = 0,
  Rb = 1001;

for (const x of S) {
  if (x < n) Lb = x;
  else if (x > n) {
    Rb = x;
    break;
  }
}

console.log((n - Lb) * (Rb - n) - 1);
