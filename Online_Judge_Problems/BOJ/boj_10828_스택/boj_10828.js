/*-----------------------------------------------------
Sub  : [BOJ] 스택
Link : https://www.acmicpc.net/problem/10828
Level: 실버 4
Tag  : JS, Stack
Memo
-----------------------------------------------------*/

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

// 스택 클래스 정의
class Stack {
  constructor() {
    this.stack = [];
  }

  isEmpty() {
    return this.stack.length === 0;
  }

  push(x) {
    this.stack.push(x);
  }

  pop() {
    return this.isEmpty() ? -1 : this.stack.pop();
  }

  size() {
    return this.stack.length;
  }

  empty() {
    return this.isEmpty() ? 1 : 0;
  }

  top() {
    return this.isEmpty() ? -1 : this.stack[this.stack.length - 1];
  }
}

// 명령어 처리
const n = parseInt(input[0]);
const commands = input.slice(1);
const stack = new Stack();
const output = [];

for (let i = 0; i < n; i++) {
  const [cmd, val] = commands[i].split(" ");
  switch (cmd) {
    case "push":
      stack.push(parseInt(val));
      break;
    case "pop":
      output.push(stack.pop());
      break;
    case "size":
      output.push(stack.size());
      break;
    case "empty":
      output.push(stack.empty());
      break;
    case "top":
      output.push(stack.top());
      break;
  }
}

console.log(output.join("\n"));
