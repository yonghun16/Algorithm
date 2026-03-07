/** 
 * -----------------------------------------------------------
 * Sub    : [BOJ] 스택2
 * Link   : https://www.acmicpc.net/problem/28278
 * Level  : Silver 4
 * Tag    : TS, Stack
 * ------------------------------------------------------------
 * Details
 * 
 * ------------------------------------------------------------
 */

import * as fs from "fs";
import * as path from "path";

const filePath: string = path.join(process.cwd(), "input_test.txt");
const input: string[] = fs.existsSync(filePath)
  ? fs.readFileSync(filePath, "utf8").trim().split(/\s+/)
  : fs.readFileSync(0, "utf8").trim().split(/\s+/);

let inputIdx: number = 0;

// 스택 인터페이스 정의
interface Stack {
  push: (x: string) => void;
  pop: () => string | number;
  size: () => number;
  isEmpty: () => 1 | 0;
  peek: () => string | number;
}

// 클로저 기반 스택 생성 함수
function createStack(): Stack {
  const items: string[] = [];

  return {
    push(x: string) {
      items.push(x);
    },
    pop() {
      const popped = items.pop();
      return popped === undefined ? -1 : popped;
    },
    size() {
      return items.length;
    },
    isEmpty() {
      return items.length === 0 ? 1 : 0;
    },
    peek() {
      return items.length === 0 ? -1 : items[items.length - 1];
    },
  };
}

// Solve
const N: number = parseInt(input[inputIdx++]);
const stack = createStack();
const results: (string | number)[] = [];

for (let i = 0; i < N; i++) {
  const cmdType = input[inputIdx++];

  switch (cmdType) {
    case "1":
      stack.push(input[inputIdx++]);
      break;
    case "2":
      results.push(stack.pop());
      break;
    case "3":
      results.push(stack.size());
      break;
    case "4":
      results.push(stack.isEmpty());
      break;
    case "5":
      results.push(stack.peek());
      break;
  }
}

// print
process.stdout.write(results.join("\n") + "\n");
