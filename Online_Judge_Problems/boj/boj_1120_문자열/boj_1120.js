/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 문자열
 * Link   : https://www.acmicpc.net/problem/
 * Level  : 실버 4
 * Tag    : JS, brute force
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

const [A, B] = input[0].split(" ");

const aLen = A.length;
const bLen = B.length;

let answer = Infinity;

// B에서 A 길이만큼 슬라이딩
for (let i = 0; i <= bLen - aLen; i++) {
  let diff = 0;

  for (let j = 0; j < aLen; j++) {
    if (A[j] !== B[i + j]) {
      diff++;
    }
  }

  answer = Math.min(answer, diff);
}

console.log(answer);
