/** -----------------------------------------------------------
 * Sub    : [Programmers] 택배 상자 꺼내기
 * Link   : https://school.programmers.co.kr/learn/courses/30/lessons/389478
 * Level  : 1
 * Tag    : TS, Math
 * ------------------------------------------------------------
 * Approach
 * - 상자 번호를 (row, col) 좌표로 변환한다.
 * - 목표 상자와 마지막 상자의 열을 비교하여 위에 존재하는 상자의 개수를 계산한다.
 * ------------------------------------------------------------
 */

declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

/* 📥 Get Input Data */
const getInputData = () => {
  const [n, w, num] = input.map(Number);

  return [n, w, num];
};

/* ⚙️ Logic */
/**
 * 상자 번호를 지그재그 적재 기준의 (row, col) 좌표로 변환한다.
 *
 * @param num 타겟 상자 번호 (1-indexed)
 * @param w 한 줄에 배치되는 상자 개수
 * @returns [row, col] (0-indexed)
 */
const getCoords = (num: number, w: number): [number, number] => {
  const row = Math.floor((num - 1) / w);
  const remainder = (num - 1) % w;

  let col: number;

  if (row % 2 === 0) {
    col = remainder;
  } else {
    col = w - 1 - remainder;
  }

  return [row, col];
};

/**
 * 타겟 상자를 꺼내기 위해 제거해야 하는 상자의 개수를 계산한다.
 *
 * @param n 전체 상자 개수
 * @param w 한 줄에 배치되는 상자 개수
 * @param num 꺼낼 상자 번호
 * @returns 제거해야 하는 상자의 개수
 */
const solution = (n: number, w: number, num: number): number => {
  const [row, col] = getCoords(num, w);
  const [lastRow, lastCol] = getCoords(n, w);

  // 꼭대기 바로 전 층까지 존재하는 상자의 개수
  let answer = lastRow - row;

  let topBoxNum: number;

  if (lastRow % 2 === 0) {
    topBoxNum = lastRow * w + col + 1;
  } else {
    topBoxNum = lastRow * w + (w - 1 - col) + 1;
  }

  // 가장 윗층의 같은 열에도 상자가 존재하는 경우
  if (topBoxNum <= n) {
    answer++;
  }

  return answer;
};

/* 🚀 Run Program */
(() => {
  const [n, w, num] = getInputData();
  console.log(solution(n, w, num));
})();
