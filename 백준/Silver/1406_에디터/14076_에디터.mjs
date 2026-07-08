/** * -----------------------------------------------------------
 * Sub    : [BOJ] 에디터
 * Link   : https://www.acmicpc.net/problem/14076
 * Level  : 실버 2
 * Tag    : JS, Stack
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

import fs from "fs";
import path from "path";

const filePath = path.join(process.cwd(), "input_test.txt");
let input;

if (fs.existsSync(filePath)) {
  input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
} else {
  input = fs.readFileSync(0, "utf-8").trim().split("\n");
}

let inputIndex = 0;

// left stack, right stack definition
const leftStack = [];
const rightStack = [];

// input
leftStack.push(...input[inputIndex++].split(""));
const m = Number(input[inputIndex++]);

// process
for (let i = 0; i < m; i++) {
  const command = input[inputIndex++];

  if (command === "L") {
    if (leftStack.length > 0) {
      rightStack.push(leftStack.pop());
    }
  } else if (command === "D") {
    if (rightStack.length > 0) {
      leftStack.push(rightStack.pop());
    }
  } else if (command === "B") {
    if (leftStack.length > 0) {
      leftStack.pop();
    }
  } else {
    leftStack.push(command[2]);
  }
}

// output
console.log(leftStack.join("") + rightStack.reverse().join(""));
