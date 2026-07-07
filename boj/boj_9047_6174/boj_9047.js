/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 6174
 * Link   : https://www.acmicpc.net/problem/9047
 * Level  : Silver 5
 * Tag    : JS, Math
 * ------------------------------------------------------------
 * Details
 * - padStart(4, '0'): 문자열이 4자리가 안 되면 앞을 '0'으로 채움
 * - sort(): 배열 정렬 (a-b는 오름차순, b-a는 내림차순)
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

// 카프리카 연산 함수
function getKaprekar(n) {
  const digits = n.toString().padStart(4, "0").split("");

  const big = parseInt([...digits].sort((a, b) => b - a).join(""));
  const small = parseInt([...digits].sort((a, b) => a - b).join(""));

  return big - small;
}

function solve() {
  // variable
  const kaprekar = 6174;
  const result = [];

  // input
  const n = parseInt(input[0]);
  const nums = [];

  for (let i = 1; i <= n; i++) {
    nums.push(input[i]);
  }

  // logic
  for (const num of nums) {
    let count = 0;
    current = num;

    while (parseInt(current) !== kaprekar) {
      current = getKaprekar(current);
      count++;
    }

    result.push(count);
  }

  // output
  console.log(result.join("\n"));
}

solve();
