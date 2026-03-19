/** * -----------------------------------------------------------
 * Sub    : [BOJ] 오큰수
 * Link   : https://www.acmicpc.net/problem/17298
 * Level  : 골드4
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

// Stack
class Stack {
  constructor() {
    this.items = [];
  }

  push(data) {
    this.items.push(data);
  }

  pop() {
    return this.items.pop();
  }

  peek() {
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }
}

// input & init
const N = Number(input[inputIdx++]);
const arr = [];
const stack = new Stack();
const result = Array(N).fill(-1);

for (let i = 0; i < N; i++) {
  arr[i] = Number(input[inputIdx++]);
}

// solve
for (let i = 0; i < N; i++) {
  while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
    let index = stack.pop();
    result[index] = arr[i];
  }
  stack.push(i);
}

// output
process.stdout.write(result.join(" ") + "\n");
