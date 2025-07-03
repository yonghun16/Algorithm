class Queue {
  constructor() {
    this.items = [];
  }

  // 큐에 요소 추가 (enqueue)
  enqueue(element) {
    this.items.push(element);
  }

  // 큐에서 요소 제거 및 반환 (dequeue)
  dequeue() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items.shift();
  }

  // 큐의 첫 번째 요소 확인 (peek)
  peek() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[0];
  }

  // 큐가 비어있는지 확인
  isEmpty() {
    return this.items.length === 0;
  }

  // 큐의 길이 반환
  size() {
    return this.items.length;
  }

  // 큐 비우기
  clear() {
    this.items = [];
  }

  // 큐 출력
  print() {
    console.log(this.items.join(' <- '));
  }
}
