/**
 * -----------------------------------------------------------
 * Sub    : [BOJ] 스택2
 * Link   : https://www.acmicpc.net/problem/28278
 * Level  : 실버 4
 * Tag    : JS, Stack, Closure
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

// 클래스 기반 스택
class Stack {
  // #은 이 변수가 클래스 내부에서만 쓰인다는 '비밀' 표시. (Private)
  #items = [];

  push(x) {
    this.#items.push(x);
  }
  pop() {
    return this.#items.length === 0 ? -1 : this.#items.pop();
  }
  size() {
    return this.#items.length;
  }
  isEmpty() {
    return this.#items.length === 0 ? 1 : 0;
  }
  peek() {
    return this.#items.length === 0 ? -1 : this.#items[this.#items.length - 1];
  }
}

// input
const N = parseInt(input[inputIdx++]);
const stack = createStack();
// const stack = new Stack();
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
