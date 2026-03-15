/** * -----------------------------------------------------------
 * Sub    : [BOJ] 단어 뒤집기 2
 * Link   : https://www.acmicpc.net/problem/17413
 * Level  : Silver 3
 * Tag    : TS, String, Stack
 * ------------------------------------------------------------
 * Details
 *
 * ------------------------------------------------------------
 */

import * as fs from "fs";
import * as path from "path";

const filePath: string = path.join(process.cwd(), "input_test.txt");
const input: string = fs.existsSync(filePath)
  ? fs.readFileSync(filePath, "utf8")
  : fs.readFileSync(0, "utf8");

let inputIdx: number = 0;

// init
let stack: string[] = [];
let result: string[] = [];
let isTag: boolean = false;

// solve
while (inputIdx < input.length) {
  const char: string = input[inputIdx];

  if (char === "\n" || char === "\r") break;

  if (char === "<") {
    while (stack.length > 0) {
      result.push(stack.pop()!);
    }
    isTag = true;
    result.push(char);
  } else if (char === ">") {
    isTag = false;
    result.push(char);
  } else if (isTag) {
    result.push(char);
  } else {
    if (char === " ") {
      while (stack.length > 0) {
        const item = stack.pop();
        if (item !== undefined) result.push(item);
      }
      result.push(char);
    } else {
      stack.push(char);
    }
  }
  inputIdx++;
}

// 남은 문자 처리
while (stack.length > 0) {
  const item = stack.pop();
  if (item !== undefined) result.push(item);
}

// print
process.stdout.write(result.join("") + "\n");
