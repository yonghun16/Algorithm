/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 두 수의 합
 * Link   : https://www.acmicpc.net/problem/3273
 * Level  : 실버 3
 * Tag    : JS, sort
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

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const x = Number(input[2]);

// 정렬
arr.sort((a, b) => a - b);

let left = 0;
let right = n - 1;
let count = 0;

while (left < right) {
  const sum = arr[left] + arr[right];

  if (sum === x) {
    count++;
    left++;
    right--;
  } else if (sum < x) {
    left++;
  } else {
    right--;
  }
}

console.log(count);
