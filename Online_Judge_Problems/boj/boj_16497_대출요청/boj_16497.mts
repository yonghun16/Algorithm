/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 대출 요청 (16497)
 * Link   : https://www.acmicpc.net/problem/16497
 * Level  : Bronze 2
 * Tag    : TypeScript (Node.js)
 * ------------------------------------------------------------
 */

import * as fs from "fs";

function solve(): void {
  // 1. 입력 처리
  // fs.readFileSync(0)은 Buffer를 반환하므로 toString() 후 처리합니다.
  const input: number[] = fs
    .readFileSync(0, "utf-8")
    .trim()
    .split(/\s+/)
    .map(Number);

  let idx: number = 0;
  const N: number = input[idx++]; // 대출 요청 건수

  // 튜플 [number, number] 타입을 가진 배열로 정의
  const requests: [number, number][] = [];
  for (let i = 0; i < N; i++) {
    const s: number = input[idx++];
    const e: number = input[idx++];
    requests.push([s, e]);
  }

  const K: number = input[idx++]; // 보유한 책의 권수

  // 2. 날짜별 대출 현황 계산 (1일 ~ 31일)
  const days: number[] = new Array(32).fill(0);

  for (const [start, end] of requests) {
    for (let i = start; i < end; i++) {
      days[i]++;
    }
  }

  // 3. 결과 판별 및 출력
  // 전개 연산자(...) 사용 시 배열이 비어있을 가능성에 대비해 초기값 0을 고려할 수 있으나,
  // 이 문제에서는 무조건 32개의 요소가 있으므로 바로 처리합니다.
  const maxRequired: number = Math.max(...days);

  console.log(maxRequired > K ? 0 : 1);
}

solve();
