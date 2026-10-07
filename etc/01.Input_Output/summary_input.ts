// 입력 패턴 모음 (TypeScript, strict + noUncheckedIndexedAccess 기준)
// 실행: npx tsx input_patterns.ts < input.txt
// 필요: npm i -D typescript tsx @types/node
// 백준 등에서 0번 fd가 안 되면 readFileSync("/dev/stdin") 으로 교체.

import { readFileSync } from "fs";
import { join } from "path";

// ───────────── 타입 ─────────────
type Pair = readonly [number, number];
type Grid<T> = readonly (readonly T[])[];

// ───────────── 공통 헬퍼 ─────────────
const readLines = (source: number | string = 0): readonly string[] =>
  readFileSync(source, "utf-8").trim().split(/\r?\n/);

const toWords = (line: string): string[] => line.trim().split(/\s+/);
const toNumbers = (line: string): number[] => toWords(line).map(Number);
const toChars = (line: string): string[] => [...line.trim()];
const toDigits = (line: string): number[] => toChars(line).map(Number);

// noUncheckedIndexedAccess 대응: 인덱스 접근 결과가 undefined면 즉시 에러
const at = <T>(items: readonly T[], index: number): T => {
  const value = items[index];
  if (value === undefined) {
    throw new RangeError(`입력이 부족합니다 (index: ${index})`);
  }
  return value;
};

// "3 5" -> readonly [3, 5] (튜플 타입으로 안전하게 언패킹)
const toPair = (line: string): Pair => {
  const nums = toNumbers(line);
  return [at(nums, 0), at(nums, 1)];
};

const take = <T>(n: number, items: readonly T[], start = 0): T[] =>
  items.slice(start, start + n);

// n줄을 parse 함수로 변환 (제네릭 고차함수)
const parseRows = <T>(
  n: number,
  lines: readonly string[],
  parse: (line: string) => T,
  start = 0,
): T[] => take(n, lines, start).map((line) => parse(line));

// 토큰 단위 리더 (입력이 크거나 줄 구조가 불규칙할 때)
const createTokenReader = (text: string) => {
  const iter = text.split(/\s+/).filter(Boolean)[Symbol.iterator]();
  const nextString = (): string => {
    const result = iter.next();
    if (result.done) throw new Error("입력이 끝났습니다");
    return result.value;
  };
  const nextNumber = (): number => Number(nextString());
  const nextNumbers = (n: number): number[] =>
    Array.from({ length: n }, nextNumber);
  return { nextString, nextNumber, nextNumbers } as const;
};

const lines = readLines();

// ───────────── 1. 숫자 하나 ─────────────
// 3
{
  const num: number = Number(at(lines, 0));
  console.log(num);
}

// ───────────── 2. 한 줄 → 각각의 숫자 변수 ─────────────
// 3 5
{
  const [a, b] = toPair(at(lines, 0));
  console.log(a, b);
}

// ───────────── 3. 한 줄 → 숫자 배열 ─────────────
// 1 2 3 4 5 6 7 8 9
{
  const arr: number[] = toNumbers(at(lines, 0));
  console.log(arr);
}

// ───────────── 4. 한 줄 → 각각의 문자열 변수 ─────────────
// abc def
{
  const words = toWords(at(lines, 0));
  const s1 = at(words, 0);
  const s2 = at(words, 1);
  console.log(s1, s2);
}

// ───────────── 5. 문자열 n줄 → 1차원 배열 ─────────────
// ABCDEF
// BCDEFA
// CDEFAB
{
  const n = 3;
  const strs: string[] = parseRows(n, lines, (line) => line.trim());
  console.log(strs);
}

// ───────────── 6. 공백 없는 숫자 n줄 → 2차원 배열 ─────────────
// 0101
// 1010
// 2020
{
  const n = 3;
  const grid: Grid<number> = parseRows(n, lines, toDigits);
  console.log(grid);
}

// ───────────── 7. 공백 구분 숫자 n줄 → 2차원 배열 ─────────────
// 0 1 0 1
// 1 0 1 0
// 2 0 2 0
{
  const n = 3;
  const matrix: Grid<number> = parseRows(n, lines, toNumbers);
  console.log(matrix);
}

// ───────────── 8. 첫 줄 T, 이후 T줄에 숫자 하나씩 ─────────────
// 3
// 1
// 2
// 3
{
  const t = Number(at(lines, 0));
  const numbers: number[] = parseRows(t, lines, Number, 1);
  console.log(numbers);
}

// ───────────── 9. 첫 줄 "n m", 이어서 n줄 격자 ─────────────
{
  const [n, m] = toPair(at(lines, 0));
  const board: Grid<number> = parseRows(n, lines, toNumbers, 1);
  console.log(n, m, board);
}

// ───────────── 10. 줄 수를 모를 때 (끝까지) ─────────────
{
  const rows: Grid<string> = lines.map(toWords); // 가변 길이 2차원 배열
  console.log(rows);
}

// ───────────── 11. 토큰 리더 (입력이 아주 클 때) ─────────────
{
  const reader = createTokenReader(readFileSync(0, "utf-8"));
  const n = reader.nextNumber();
  const arr: number[] = reader.nextNumbers(n);
  console.log(arr);
}

// ───────────── 12. 입력 파일을 직접 읽기 (로컬 테스트용) ─────────────
{
  const fileLines = readLines(join(__dirname, "input.txt"));
  const t = Number(at(fileLines, 0));
  console.log(parseRows(t, fileLines, Number, 1));
}

// ───────────── 참고: solve / main 분리 ─────────────
const solve = (n: number, arr: readonly number[]): number =>
  arr.slice(0, n).reduce((acc, x) => acc + x, 0);

export { solve };
