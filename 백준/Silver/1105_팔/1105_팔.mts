/** -----------------------------------------------------------
 * Sub    : [BOJ] 팔 (1105)
 * Link   : https://www.acmicpc.net/problem/1105
 * Level  : Silver 1
 * Tag    : TS, Greedy, Math
 * ------------------------------------------------------------
 * Solution
 * 1. L과 R의 자릿수(길이)가 다르면 무조건 8이 없는 수를 만들 수 있으므로 0을 출력합니다.
 * 2. 길이가 같다면, 가장 큰 자릿수(왼쪽)부터 하나씩 비교합니다.
 * 3. 두 숫자가 '8'로 같으면 카운트를 1 증가시킵니다.
 * 4. 두 숫자가 달라지는 순간, 그 하위 자릿수에서는 8을 무조건 피할 수 있으므로 탐색을 종료합니다.
 * ------------------------------------------------------------
 */

import * as fs from "fs";

const filePath: string = fs.existsSync("./input_test.txt")
  ? "./input_test.txt"
  : "/dev/stdin";

const input: string[] = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

// 전역 변수 선언
let L: string = "";
let R: string = "";

// 📥 Get Input Data
const getInputData = () => {
  // input 배열에서 L과 R을 추출하여 전역 변수에 할당합니다.
  if (input.length >= 2) {
    L = input[0];
    R = input[1];
  }
};

// ⚙️ Core Logic
const solution = () => {
  // 입력이 제대로 들어오지 않은 경우 방지
  if (!L || !R) return;

  // 1. 자릿수 길이가 다르면 0
  if (L.length !== R.length) {
    console.log(0);
    return;
  }

  // 2. 자릿수가 같을 때만 왼쪽부터 비교
  let countEight: number = 0;
  for (let i = 0; i < L.length; i++) {
    if (L[i] === R[i]) {
      if (L[i] === "8") {
        countEight++;
      }
    } else {
      // 숫자가 달라지는 순간 탐색 종료
      break;
    }
  }

  console.log(countEight);
};

// 🚀 Run Program
(() => {
  getInputData();
  solution();
})();
