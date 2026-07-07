// 정수 명령 처리 8 (이중 연결 리스트)

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

// 이중 연결 리스트 클래스
class DoubleLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.nodeNum = 0;
  }

  // 원소를 첫 번째 위치에 넣는다.
  pushFront(newData) {
    const newNode = new Node(newData); // 새로운 노드 생성
    newNode.next = this.head; // 새로운 노드의 next 값을 head로 바꿈.

    if (this.head != null) {
      this.head.prev = newNode; // 이전 head의 prev값을 바꾼 뒤
      this.head = newNode; // head값을 변경함.
    } else {  // 기존 리스트가 비어 있다면, 
      this.head = newNode; // head, tail을 새로 설정함.
      this.tail = newNode;
    }
    newNode.prev = null;

    this.nodeNum += 1;
  }

  // 원소를 맨 끝 위치에 넣어줍니다.
  pushBack(newData) { 
    const newNode = new Node(newData);  // 새로운 노드를 만들어줍니다.
    newNode.prev = this.tail; // 새로운 노드의 prev 값을 tail로 바꿔줌.

    if (this.tail != null) {  // 기존 리스트가 비어있지 않았다면
      this.tail.next = newNode;  // 이전 tail의 next값을 바꾼 
      this.tail = newNode;  // tail 값을 변경해줍니다.
    } else {
      this.head = newNode; // head, tail을 새로 설정해줍니다.
      this.tail = newNode;
    }
    newNode.next = null;

    this.nodeNum += 1;
  }

  // 첫 번째 수를 빼면서, 동시에 그 수를 반환합니다.
  popFront() {
    if (this.head == null) {
      console.log("List is empty");
      return null;
    } else if (this.head.next == null) {  // 노드가 하나 남았다면
      const temp = this.head;

      this.head = null;  // head값을 None으로 바꿔주고
      this.tail = null;  // tail값도 None으로 바꺼주고
      this.nodeNum = 0;  // 원소의 수도 0개로 변경해줍니다.

      return temp.data;
    } else {
      const temp = this.head;
      temp.next.prev = null;  // 새로 head가 될 노드의 prev값을 지워줍니다.
      this.head = temp.next;  // head값을 새로 갱신해주고
      temp.next = null; // 이전 head의 next 값을 지워줍니다.

      this.nodeNum -= 1;
    }
  }

  // 맨 끝에 있는 수를 빼면서 동시에 그 수를 반환합니다.
  popBack() {
    if (this.tail == null) {
      console.log("List is empty");
    } else if (this.tail.prev == null) { // 노드가 하나 남았다면
      const temp = this.tail;

      this.head = null;  // head값을 None으로 바꿔주고
      this.tail = null;  // tail값도 None으로 바꿔주고
      this.nodeNum = 0;  // 원소의 수도 0개로 변경해줍니다.

      return temp.data;
    } else {
      const temp = this.tail;
      temp.prev.next = null;  // 새로 tail이 될 노드의 next값을 지워줍니다.
      this.tail = temp.prev; // tail값을 새로 갱신해주고
      temp.prev = null;  // 이전 tail의 prev 값을 지워줍니다.

      this.nodeNum -= 1;
      return temp.data;
    }
  }

  // 크기 출력
  size() {
    return this.nodeNum;
  }

  // 비어있는지 확인
  empty() {
    return this.nodeNum == 0;
  }

  // 첫 번째 수를 반환합니다.
  front() {
    if (this.head == null) {
      console.log("List is empty");
      return null;
    } else {
      return this.head.data;
    }
  }

  // 맨 끝에 있는 수를 반환합니다.
  back() {
    if (this.tail == null) {
      console.log("List is empty");
    } else {
      return this.tail.data;
    }
  }

  // 노드 관계 출력
  print() {
    let result = [];
    let current = this.head;
    while (current !== null) {
      result.push(current.data);
      current = current.next;
    }
    console.log("Forward:", result.join(" -> "));

    result = [];
    current = this.tail;
    while (current !== null) {
      result.push(current.data);
      current = current.prev;
    }
    console.log("Backward:", result.join(" -> "));
  }
}


// 테스트

const dll = new DoubleLinkedList();
dll.pushFront(1);
dll.pushFront(2);
dll.pushFront(3);
dll.pushBack(4);
dll.print();
console.log(dll.size());
