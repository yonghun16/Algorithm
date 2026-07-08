/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 분수찾기
 * Link   : https://www.acmicpc.net/problem/1193
 * Level  : 실버 5
 * Tag    : JS, Math
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

const X = Number(input[0]);

let line = 1;
// 누적 개수가 X 이상이 되는 첫 번째 line 찾기
while (X > (line * (line + 1)) / 2) {
  line++;
}

const totalBefore = (line * (line - 1)) / 2;
const offset = X - totalBefore; // line의 몇 번째 위치인지

let numerator, denominator;

// line이 홀수: 위 → 아래
if (line % 2 === 1) {
  numerator = line - (offset - 1);
  denominator = offset;
}
// line이 짝수: 아래 → 위
else {
  numerator = offset;
  denominator = line - (offset - 1);
}

console.log(`${numerator}/${denominator}`);
