/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 스택2
 * Link   : https://www.acmicpc.net/problem/28278
 * Level  : 실버 4
 * Tag    : JS, Stack, Closure
 * ------------------------------------------------------------
 */

const fs = require("fs");
const path = require("path");

const filePath = path.join(process.cwd(), "input_test.txt");
const input = fs.existsSync(filePath)
  ? fs.readFileSync(filePath, "utf8").trim().split(/\s+/)
  : fs.readFileSync(0, "utf8").trim().split(/\s+/);

let inputIdx = 0;

// 클로저 기반 스택 생성 함수
function createStack() {
  const items = [];

  return {
    push(x) {
      items.push(x);
    },
    pop() {
      return items.length === 0 ? -1 : items.pop();
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

// input
const N = parseInt(input[inputIdx++]);
const stack = createStack();
const results = [];

// solve
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

// output
process.stdout.write(results.join("\n") + "\n");
