class Stack {
  constructor() {
    this.items = [];
  }

  // 스택에 요소 추가 (push)
  push(element) {
    this.items.push(element);
  }

  // 스택에서 요소 제거 및 반환 (pop)
  pop() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items.pop();
  }

  // 스택 최상단 요소 반환 (peek)
  peek() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.items.length - 1];
  }

  // 스택이 비었는지 확인 (isEmpty)
  isEmpty() {
    return this.items.length === 0;
  }

  // 스택의 크기 확인 (size)
  size() {
    return this.items.length;
  }

  // 스택 비우기 (clear)
  clear() {
    this.items = [];
  }

  // 스택 전체 출력 (for debugging)
  print() {
    console.log(this.items.join(' <- '));
  }
}

// 예시 사용
const stack = new Stack();

stack.push(10);
stack.push(20);
stack.push(30);

stack.print();        // 10 <- 20 <- 30

console.log(stack.pop());   // 30
console.log(stack.peek());  // 20
console.log(stack.size());  // 2
console.log(stack.isEmpty()); // false

stack.clear();
console.log(stack.isEmpty()); // true
