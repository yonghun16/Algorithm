/**
 * -----------------------------------------------------------
 * Sub    : [Programmers] 덧칠하기
 * Link   : https://school.programmers.co.kr/learn/courses/30/lessons/161989
 * Level  : Lv.1
 * Tag    : JS, Greedy
 * ------------------------------------------------------------
 * Solution
 * 가장 왼쪽의 미칠 구역부터 시작해서
 * 길이 m만큼 한 번에 칠하며 커버 범위를 갱신한다.
 * ------------------------------------------------------------
 */

const fs = require("fs");

const filePath = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input = fs.readFileSync(filePath, "utf-8").trim().split("\n");

// 📥 Get Input Data
const getInputData = () => {
  const n = Number(input[0]);
  const m = Number(input[1]);

  // "2, 3, 6" → [2, 3, 6]
  const section = input[2].split(",").map((v) => Number(v.trim()));

  return { n, m, section };
};

// ⚙️ Core Logic
const solution = (n, m, section) => {
  let answer = 0;
  let paintedEnd = 0;

  for (const s of section) {
    if (s > paintedEnd) {
      answer++;
      paintedEnd = s + m - 1;
    }
  }

  return answer;
};

// 🚀 Run Program
(() => {
  const { n, m, section } = getInputData();
  console.log(solution(n, m, section));
})();
