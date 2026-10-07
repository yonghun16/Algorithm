"use strict";

// 입력 패턴 모음 (Node.js). 패턴별로 필요한 부분만 복사해서 사용.
// 백준 등에서 0 번 fd가 안 되면 readFileSync("/dev/stdin") 으로 교체.
const { readFileSync } = require("fs");

// ───────────── 공통 헬퍼 (작은 순수 함수들) ─────────────
const readLines = (source = 0) =>
  readFileSync(source, "utf-8").trim().split(/\r?\n/); // Windows(CRLF)도 안전하게 처리

const toWords = (line) => line.trim().split(/\s+/); // 'abc def' -> ['abc','def']
const toNumbers = (line) => toWords(line).map(Number); // '3 5' -> [3, 5]
const toChars = (line) => [...line.trim()]; // 'ABC' -> ['A','B','C']
const toDigits = (line) => toChars(line).map(Number); // '0101' -> [0,1,0,1]

const take = (n, lines, start = 0) => lines.slice(start, start + n);

const lines = readLines();

// ───────────── 1. 숫자 하나 ─────────────
// 3
{
  const num = Number(lines[0]);
  console.log(num);
}

// ───────────── 2. 한 줄 → 각각의 숫자 변수 ─────────────
// 3 5
{
  const [a, b] = toNumbers(lines[0]);
  console.log(a, b);
}

// ───────────── 3. 한 줄 → 숫자 배열 ─────────────
// 1 2 3 4 5 6 7 8 9
{
  const arr = toNumbers(lines[0]);
  console.log(arr);
}

// ───────────── 4. 한 줄 → 각각의 문자열 변수 ─────────────
// abc def
{
  const [s1, s2] = toWords(lines[0]);
  console.log(s1, s2);
}

// ───────────── 5. 문자열 n줄 → 1차원 배열 ─────────────
// ABCDEF
// BCDEFA
// CDEFAB
{
  const n = 3;
  const strs = take(n, lines).map((line) => line.trim());
  console.log(strs);
}

// ───────────── 6. 공백 없는 숫자 n줄 → 2차원 배열 ─────────────
// 0101
// 1010
// 2020
{
  const n = 3;
  const grid = take(n, lines).map(toDigits);
  console.log(grid);
}

// ───────────── 7. 공백 구분 숫자 n줄 → 2차원 배열 ─────────────
// 0 1 0 1
// 1 0 1 0
// 2 0 2 0
{
  const n = 3;
  const matrix = take(n, lines).map(toNumbers);
  console.log(matrix);
}

// ───────────── 8. 첫 줄 T, 이후 T줄에 숫자 하나씩 ─────────────
// 3
// 1
// 2
// 3
{
  const [first, ...rest] = lines; // 구조 분해 + 나머지 요소
  const numbers = take(Number(first), rest).map(Number);
  console.log(numbers);
}

// ───────────── 9. 첫 줄 "n m", 이어서 n줄 격자 ─────────────
{
  const [[n, m], ...rows] = lines.map(toNumbers);
  const board = take(n, rows);
  console.log(n, m, board);
}

// ───────────── 10. 줄 수를 모를 때 (끝까지) ─────────────
{
  const rows = lines.map(toWords); // 가변 길이 2차원 배열
  console.log(rows);
}

// ───────────── 11. 입력이 아주 클 때: 토큰 단위 이터레이터 ─────────────
{
  const tokens = readFileSync(0, "utf-8").split(/\s+/).filter(Boolean);
  const iter = tokens.values();
  const next = () => iter.next().value;
  const n = Number(next());
  const arr = Array.from({ length: n }, () => Number(next()));
  console.log(arr);
}

// ───────────── 12. 입력 파일을 직접 읽기 (로컬 테스트용) ─────────────
{
  const { join } = require("path");
  const fileLines = readLines(join(__dirname, "input.txt"));
  const [t, ...rest] = fileLines;
  console.log(take(Number(t), rest).map(Number));
}
