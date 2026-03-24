/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 좋은 단어
 * Link   : https://www.acmicpc.net/problem/3986
 * Level  : Silver 3
 * Tag    : TS, Stack
 * ------------------------------------------------------------
 */

import * as fs from "fs";
import * as path from "path";

const filePath: string = path.join(process.cwd(), "input_test.txt");

const input: string[] = fs.existsSync(filePath)
  ? fs.readFileSync(filePath, "utf8").trim().split(/\s+/)
  : fs.readFileSync(0, "utf8").trim().split(/\s+/);

let inputIdx: number = 0;

// input & init
const n: number = Number(input[inputIdx++]);
let answer: number = 0;

// solve
for (let i = 0; i < n; i++) {
  const word: string = input[inputIdx++];
  const stack: string[] = [];

  for (const char of word) {
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
