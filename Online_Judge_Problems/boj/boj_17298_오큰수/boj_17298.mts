/** * -----------------------------------------------------------
 * Sub    : [BOJ] 오큰수
 * Link   : https://www.acmicpc.net/problem/17298
 * Level  : 골드4
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

// stack
class Stack<T> {
  private items: T[] = [];

  constructor() {
    this.items = [];
  }

  push(data: T): void {
    this.items.push(data);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }
}

// input & init
const N: number = Number(input[inputIdx++]);
const arr: number[] = [];
const stack = new Stack<number>();
const result: number[] = Array(N).fill(-1);

for (let i = 0; i < N; i++) {
  arr[i] = Number(input[inputIdx++]);
}

// solve
for (let i = 0; i < N; i++) {
  while (!stack.isEmpty()) {
    const topIdx = stack.peek();
    if (topIdx !== undefined && arr[topIdx] < arr[i]) {
      const index = stack.pop()!;
      result[index] = arr[i];
    } else {
      break;
    }
  }
  stack.push(i);
}

// output
process.stdout.write(result.join(" ") + "\n");
