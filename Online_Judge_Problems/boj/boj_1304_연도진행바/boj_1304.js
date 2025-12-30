/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 연도 진행바
 * Link   : https://www.acmicpc.net/problem/1304
 * Level  : 실버 5
 * Tag    : JS, 구현
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

let input;

if (process.platform === "linux") {
  input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
} else {
  const path = require("path");
  const filePath = path.join(__dirname, "input.txt");
  input = require("fs").readFileSync(filePath, "utf-8").trim().split("\n");
}

function solve() {
  // 입력 파싱: "May 10, 1981 00:31"
  // 콤마와 콜론을 공백으로 치환하여 쉽게 분리
  const line = input[0].replace(",", "").replace(":", " ");
  const parts = line.split(/\s+/);

  const monthStr = parts[0];
  const day = parseInt(parts[1]);
  const year = parseInt(parts[2]);
  const hour = parseInt(parts[3]);
  const minute = parseInt(parts[4]);

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  // 윤년 판별 함수
  const isLeap = (y) => {
    return (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0;
  };

  if (isLeap(year)) {
    daysInMonth[1] = 29;
  }

  // 1. 해당 연도의 전체 분 계산
  const totalDays = isLeap(year) ? 366 : 365;
  const totalMinutes = totalDays * 24 * 60;

  // 2. 현재까지 흐른 분 계산
  let elapsedDays = 0;
  const monthIndex = months.indexOf(monthStr);

  // 지난 달까지의 일수 합산
  for (let i = 0; i < monthIndex; i++) {
    elapsedDays += daysInMonth[i];
  }

  // 현재 달의 일수 합산 (오늘 날짜는 아직 다 안 지났으므로 day - 1)
  elapsedDays += day - 1;

  const elapsedMinutes = elapsedDays * 24 * 60 + hour * 60 + minute;

  // 3. 결과 출력 (백분율)
  const result = (elapsedMinutes / totalMinutes) * 100;
  console.log(result);
}

solve();
