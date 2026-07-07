/** * -----------------------------------------------------------
 * Sub    : [BOJ] 단어 뒤집기 2
 * Link   : https://www.acmicpc.net/problem/17413
 * Level  : Silver 3
 * Tag    : JS, String, Stack
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

const fs = require("fs");
const path = require("path");

const filePath = path.join(process.cwd(), "input_test.txt");
const input = fs.existsSync(filePath)
  ? fs.readFileSync(filePath, "utf8")
  : fs.readFileSync(0, "utf8");

let inputIdx = 0;

// init
let stack = [];
let result = [];
let isTag = false;

// solve
while (inputIdx < input.length) {
  let char = input[inputIdx];

  if (char === "\n" || char === "\r") break;

  if (char === "<") {
    while (stack.length > 0) {
      result.push(stack.pop());
    }
    isTag = true;
    result.push(char); // '<' 추가
  } else if (char === ">") {
    isTag = false;
    result.push(char); // '>' 추가
  } else if (isTag) {
    result.push(char);
  } else {
    if (char === " ") {
      while (stack.length > 0) {
        result.push(stack.pop());
      }
      result.push(char); // 공백 본인 추가
    } else {
      stack.push(char);
    }
  }
  inputIdx++;
}

while (stack.length > 0) {
  result.push(stack.pop());
}

// print
process.stdout.write(result.join("") + "\n");
