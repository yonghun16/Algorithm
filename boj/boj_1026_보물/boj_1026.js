/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 보물
 * Link   : https://www.acmicpc.net/problem/1026
 * Level  : 실버 4
 * Tag    : JS, Greedy
 * Memo
 * -----------------------------------------------------------
 */

const TEST_MODE = true;
let rawLines;

if (TEST_MODE) {
  const filePath = require("path").join(__dirname, "input.txt");
  rawLines = require("fs").readFileSync(filePath, "utf8").trim().split("\n");
} else {
  rawLines = require("fs").readFileSync(0, "utf8").trim().split("\n");
}

// 첫 줄은 N (숫자)
const N = Number(rawLines[0].trim());

// 둘째 줄과 셋째 줄은 공백으로 구분된 숫자들
const A = rawLines[1].trim().split(/\s+/).map(Number);
const B = rawLines[2].trim().split(/\s+/).map(Number);

// A 오름차순, B 내림차순
A.sort((a, b) => a - b);
B.sort((a, b) => b - a);

let result = 0;
for (let i = 0; i < N; i++) {
  result += A[i] * B[i];
}

console.log(result);
