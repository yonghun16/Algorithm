/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 토너먼트
 * Link   : https://www.acmicpc.net/problem/1057
 * Level  : 실버 4
 * Tag    : JS, Math
 * Memo
 * -----------------------------------------------------------
 */

// [환경 설정]
const TEST_MODE = true;
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

// 입력 처리
let [N, a, b] = input[0].split(" ").map(Number);

let round = 0;

// 둘이 같은 번호가 될 때까지
while (a !== b) {
  a = Math.ceil(a / 2);
  b = Math.ceil(b / 2);
  round++;

  // 말도 안 되게 끝까지 못 만나면 -1 처리 (실제로 이런 경우는 없음)
  if (round > 20) break;
}

console.log(a === b ? round : -1);
