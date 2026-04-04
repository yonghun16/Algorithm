/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 대출 요청 (16497)
 * Link   : https://www.acmicpc.net/problem/16497
 * Level  : Bronze 2
 * Tag    : JavaScript (Node.js)
 * ------------------------------------------------------------
 */

const fs = require("fs");

function solve() {
  // 1. 입력 처리: 표준 입력(0)으로부터 전체 데이터를 읽어와 공백 단위로 분리합니다.
  const input = fs.readFileSync(0, "utf-8").trim().split(/\s+/).map(Number);

  let idx = 0;
  const N = input[idx++]; // 대출 요청 건수

  const requests = [];
  for (let i = 0; i < N; i++) {
    const s = input[idx++];
    const e = input[idx++];
    requests.push([s, e]);
  }

  const K = input[idx++]; // 보유한 책의 권수

  // 2. 날짜별 대출 현황 계산 (1일 ~ 31일)
  // Array.fill을 이용해 0으로 초기화된 배열을 생성합니다.
  const days = new Array(32).fill(0);

  for (const [start, end] of requests) {
    // 반납일 당일(end)은 대출 가능 상태이므로 end 전까지만 카운트합니다.
    for (let i = start; i < end; i++) {
      days[i]++;
    }
  }

  // 3. 결과 판별 및 출력
  // Math.max(...array)를 사용하여 배열의 최댓값을 구합니다.
  const maxRequired = Math.max(...days);

  console.log(maxRequired > K ? 0 : 1);
}

solve();
