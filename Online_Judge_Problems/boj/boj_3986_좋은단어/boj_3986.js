/** * -----------------------------------------------------------
 * Sub    : [BOJ] 좋은 단어
 * Link   : https://www.acmicpc.net/problem/3986
 * Level  : Silver 3
 * Tag    : JS, Stack
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

const fs = require("fs");
const path = require("path");

const filePath = path.join(process.cwd(), "input_test.txt");
const input = fs.existsSync(filePath)
  ? fs.readFileSync(filePath, "utf8").trim().split(/\s+/)
  : fs.readFileSync(0, "utf8").trim().split(/\s+/);

let inputIdx = 0;

// input & init
n = Number(input[inputIdx++]);
let answer = 0;

// solve
for (let i = 0; i < n; i++) {
  word = input[inputIdx++];
  const stack = [];

  for (let char of word) {
    if (stack.length > 0 && stack[stack.length - 1] === char) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  if (stack.length === 0) {
    answer += 1;
  }
}

// print
console.log(answer);
