/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 더하기 2 (10823)
 * Link   : https://www.acmicpc.net/problem/10823
 * Level  : Bronze 2
 * Tag    : JavaScript, Node.js, String, Parsing
 * -----------------------------------------------------------
 * Solution
 * 1. fs.readFileSync를 통해 전체 입력을 가져옵니다.
 * 2. 모든 공백(줄바꿈 포함)을 제거하여 끊어진 숫자들을 하나로 잇습니다.
 * 3. 콤마를 기준으로 분리한 뒤 숫자로 변환하여 합산합니다.
 * -----------------------------------------------------------
 */

const fs = require("fs");

const filePath = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const rawInput = fs.readFileSync(filePath, "utf-8");

// 📥 Get Input Data
const getInputData = () => {
  let combinedString = rawInput.replace(/\s/g, "");

  return combinedString;
};

// ⚙️ Core Logic
const solution = (combinedString) => {
  if (!combinedString) return;

  const totalSum = combinedString
    .split(",")
    .filter((val) => val.length > 0)
    .reduce((acc, cur) => acc + Number(cur), 0);

  console.log(totalSum);
};

// 🚀 Run Program
(() => {
  const combinedString = getInputData();
  solution(combinedString);
})();
