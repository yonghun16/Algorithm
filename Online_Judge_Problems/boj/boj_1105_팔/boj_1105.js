/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 팔 (1105)
 * Link   : https://www.acmicpc.net/problem/1105
 * Level  : Silver 1
 * Tag    : JS, Greedy, Math
 * ------------------------------------------------------------
 * Solution
 * 1. L과 R의 자릿수(길이)가 다르면 그 사이에 반드시 8이 없는 숫자가 존재합니다. (예: 88~100 사이 90)
 * 2. 자릿수가 같다면 왼쪽(큰 자릿수)부터 비교합니다.
 * 3. 숫자가 서로 같다면 그 숫자가 '8'일 때만 카운트합니다.
 * 4. 숫자가 달라지는 순간, 그 뒤로는 숫자를 조절해 8을 안 쓸 수 있으므로 즉시 종료합니다.
 * ------------------------------------------------------------
 */

const fs = require("fs");

// 로컬 테스트 파일이 없다면 백준 환경(0)으로 자동 인식되도록 설정
const filePath = fs.existsSync("./input_test.txt") ? "./input_test.txt" : 0;

// 입력을 깔끔하게 읽고 공백 기준으로 나눔
const input = fs.readFileSync(filePath, "utf-8").trim().split(/\s+/);

const solution = () => {
  // 입력값이 정상적으로 2개 들어오지 않은 경우 예외 처리
  if (input.length < 2) return;

  const L = input;
  const R = input;

  // 1. 자릿수가 다르면 무조건 0
  if (L.length !== R.length) {
    console.log(0);
    return;
  }

  // 2. 자릿수가 같을 때만 왼쪽부터 비교
  let countEight = 0;
  for (let i = 0; i < L.length; i++) {
    if (L[i] === R[i]) {
      if (L[i] === "8") countEight++;
    } else {
      break; // 숫자가 달라지는 순간 8을 회피할 수 있으므로 탐색 종료
    }
  }

  console.log(countEight);
};

solution();
