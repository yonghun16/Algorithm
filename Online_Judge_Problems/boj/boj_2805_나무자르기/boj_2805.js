/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 나무 자르
 * Link   : https://www.acmicpc.net/problem/2805
 * Level  : 실버 2
 * Tag    : JS, 이분 탐색
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

const [N, M] = input[0].split(" ").map(Number);
const trees = input[1].split(" ").map(Number);

// 이분 탐색 범위: 최소 0, 최대 나무 최대 높이
let left = 0;
let right = Math.max(...trees);
let answer = 0;

while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  let sum = 0;

  for (let h of trees) {
    if (h > mid) {
      sum += h - mid; // 나무들의 최고 높이 - 자르는 높이의 합
    }
  }

  // sum >= M 이면 더 높이 자를 수 있다 (답이 될 가능성 있음)
  if (sum >= M) {
    answer = mid;
    left = mid + 1;
  } else {
    right = mid - 1;
  }
}

console.log(answer);
