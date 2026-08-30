/** -----------------------------------------------------------
 * Sub    : [Programmers] 공원
 * Link   : https://school.programmers.co.kr/learn/courses/30/lessons/340198
 * Level  : 1
 * Tag    : TS, Simulation
 * ------------------------------------------------------------
 * Approach
 * - 돗자리 크기 리스트(mats)와 공원 배치도(park)를 입력받음.
 * - 돗자리를 큰 것부터 순서대로 시도.
 * - 각 크기마다 공원의 모든 시작 위치 (i, j)를 완전탐색.
 * - 해당 위치에서 size x size 정사각형 범위가 전부 "-1"이면
 *   그 크기를 바로 정답으로 반환 (큰 것부터 시도했으므로 첫 성공이 최댓값).
 * - 끝까지 깔 수 있는 위치가 없으면 -1 반환.
 * ------------------------------------------------------------
 */

declare var require: any;
const fs: any = require("fs");

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\n+/);

/* 📥 Input */
const getInputData = (): { mats: number[]; park: string[][] } => {
  const mats: number[] = input[0].split(" ").map(Number);
  const park: string[][] = input.slice(1).map((line) => line.split(" "));
  return { mats, park };
};

/* ⚙️ Logic */
const canPlace = (
  park: string[][],
  i: number,
  j: number,
  size: number,
): boolean => {
  for (let di = 0; di < size; di++) {
    for (let dj = 0; dj < size; dj++) {
      if (park[i + di][j + dj] !== "-1") return false;
    }
  }
  return true;
};

const solution = (mats: number[], park: string[][]): number => {
  const height: number = park.length;
  const width: number = park[0].length;

  const sortedMats: number[] = [...mats].sort((a, b) => b - a);

  for (const size of sortedMats) {
    for (let i = 0; i <= height - size; i++) {
      for (let j = 0; j <= width - size; j++) {
        if (canPlace(park, i, j, size)) return size;
      }
    }
  }

  return -1;
};

/* 🚀 Run Program */
(() => {
  const { mats, park } = getInputData();
  console.log(solution(mats, park));
})();
