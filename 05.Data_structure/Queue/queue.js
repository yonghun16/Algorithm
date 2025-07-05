class Queue {
  constructor() {
    this.items = {};
    this.headIndex = 0;
    this.tailIndex = 0;
  }

  enqueue(item) {
    this.items[this.tailIndex] = item;
    this.tailIndex++;
  }

  dequeue() {
    const item = this.items[this.headIndex];
    delete this.items[this.headIndex];
    this.headIndex++;
    return item;
  }

  peek() {
    return this.items[this.headIndex];
  }

  getLength() {
    return this.tailIndex - this.headIndex;
  }
}


// 큐  생성
const queue = new Queue();


// 출 입력
queue.enqueue(4);
queue.enqueue(5);
queue.enqueue(2);


// 큐 출력
while (queue.getLength() > 0) {
  console.log(queue.dequeue());
}

