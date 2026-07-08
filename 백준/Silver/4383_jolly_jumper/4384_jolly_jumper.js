/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 점프는 즐거워
 * Link   : https://www.acmicpc.net/problem/4383
 * Level  : 실버 5
 * Tag    : JS, 구현
 * ------------------------------------------------------------
 * Details
  - 수열 길이가 n
  - 인접한 두 수의 절댓값 차이를 구함
  -	그 차이들이 1부터 n-1까지 한 번씩 모두 등장하면 Jolly
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

let result = [];

for (const line of input) {
  if (line.trim() === "") continue;

  const arr = line.trim().split(/\s+/).map(Number);
  const n = arr[0];
  const nums = arr.slice(1);

  if (n === 1) {
    result.push("Jolly");
    continue;
  }

  const diffSet = new Set();
  let isJolly = true;

  for (let i = 1; i < n; i++) {
    const diff = Math.abs(nums[i] - nums[i - 1]);

    if (diff < 1 || diff > n - 1) {
      isJolly = false;
      break;
    }
    diffSet.add(diff);
  }

  result.push(isJolly && diffSet.size === n - 1 ? "Jolly" : "Not jolly");
}

console.log(result.join("\n"));
