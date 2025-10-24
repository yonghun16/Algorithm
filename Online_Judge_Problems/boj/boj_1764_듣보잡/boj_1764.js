/* ------------------------------------------------------------
 * Sub       : [BOJ] 듣보잡
 * Link      : https://www.acmicpc.net/problem/1764
 * Level     : 실버 4
 * Tag       : JS, map, 자료구조
 * Memo
 * -----------------------------------------------------------*/

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

const [N, M] = input[0].split(" ").map(Number);
const unheard = new Set(input.slice(1, N + 1));
const unseen = input.slice(N + 1);

const result = [];

for (const name of unseen) {
  if (unheard.has(name)) result.push(name);
}

result.sort();

console.log(result.length);
console.log(result.join("\n"));
