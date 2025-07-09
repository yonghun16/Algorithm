// singly Linked List

class Node {
  constructor(data) {
    this.data = null;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  // 맨 앞의 노드 삽입
  insertAtHead(data) {
    const newNode = new Node(data);
    newNode.next = this.head;
    this.head = newNode;
  }

  // 맨 뒤에 노드 삽입
  insertAtTail(data) {
    const newNode = new Node(data);
    if (!this.head) {  // 비어있는 리스트의 경우
      this.head = newNode;
      return;
    }
    let curr = this.head;
    while (curr.next) {
      curr = curr.next;
    }
    curr.next = newNode;
  }

  // 맨 앞 노드 삭제
  deleteAtHead() {
    if (!this.head) return;
    this.head = this.head.next;
  }


  // 맨 뒤 노드 삭제
  deleteAtTail() {
    if (!this.head) return;  // 비어있는 리스트의 경우 -> 삭제 할게 없다.
    if (!this.head.next) {   // 리스트에 1개만 있는 경우 -> head를 삭제한다.
      this.head = null;
      return;
    }
    let prev = null;
    let curr = this.head;
    while (curr.next) {     // 다음 노드로 넘김.
      prev = curr;
      curr = curr.next;
    }
    prev.next = null; 
  }

  // 노트 탐색
  search(data) {
    let curr = this.head;
    while (curr) {
      if (curr.data === data) return true;
      curr = curr.next;
    }
    return false;
  }

  // 노드 출력
  print() {
    let curr = this.head;
    let result = '';
    while (curr) {
      result += curr.data + (curr.next ? ' → ' : '');
      curr = curr.next;
    }
    console.log(result || '(empty)');
  }
}

// 테스트
const list = new LinkedList();

list.insertAtHead(10);    // 10
list.insertAtHead(20);    // 20 → 10
list.insertAtTail(30);    // 20 → 10 → 30
list.print();

list.deleteAtHead();      // 10 → 30
list.print();

list.deleteAtTail();      // 10
list.print();

console.log(list.search(10));  // true
console.log(list.search(99));  // false
