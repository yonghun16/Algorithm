/** * -----------------------------------------------------------
 * Sub    : [BOJ] 에디터
 * Link   : https://www.acmicpc.net/problem/14076
 * Level  : 실버 2
 * Tag    : TS, Stack
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

import * as fs from "fs";
import * as path from "path";

const filePath: string = path.join(process.cwd(), "input_test.txt");
let input: string[];

if (fs.existsSync(filePath)) {
  input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
} else {
  input = fs.readFileSync(0, "utf-8").trim().split("\n");
}

let inputIndex: number = 0;

// left stack, right stack definition
const rightStack: string[] = [];
const leftStack: string[] = [];

// input
leftStack.push(...input[inputIndex++].split(""));
const m: number = Number(input[inputIndex++]);

// process
for (let i = 0; i < m; i++) {
  const command: string = input[inputIndex++];

  if (command === "L") {
    if (leftStack.length > 0) {
      const char = leftStack.pop();
      if (char !== undefined) rightStack.push(char);
    }
  } else if (command === "D") {
    if (rightStack.length > 0) {
      const char = rightStack.pop();
      if (char !== undefined) leftStack.push(char);
    }
  } else if (command === "B") {
    if (leftStack.length > 0) {
      leftStack.pop();
    }
  } else if (command.startsWith("P")) {
    const charToPush = command.split(" ")[1];
    leftStack.push(charToPush);
  }
}

// output
console.log(leftStack.join("") + rightStack.reverse().join(""));
