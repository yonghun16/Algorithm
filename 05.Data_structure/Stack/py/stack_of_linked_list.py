from typing import Optional

# Node 클래스: 연결 리스트의 노드를 나타냄
class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.next: Optional["Node"] = None  # 다음 노드를 가리키는 포인터

# Stack 클래스: 연결 리스트를 이용한 스택 구현
class Stack:
    def __init__(self):
        self.head: Optional[Node] = None  # 스택의 최상단(head)을 가리킴

    # 원소 삽입 (push): 스택의 top에 데이터를 추가
    def push(self, data):
        new_node = Node(data)  # 새로운 노드 생성
        new_node.next = self.head  # 새 노드는 현재 head를 가리킴
        self.head = new_node  # head를 새 노드로 갱신

    # 원소 추출 (pop): 스택의 top에서 데이터를 제거
    def pop(self):
        if self.is_empty():
            return None  # 스택이 비어있으면 None 반환

        data = self.head.data  # head에 있는 데이터를 저장
        self.head = self.head.next  # head를 다음 노드로 갱신

        return data  # 제거한 데이터를 반환

    # 최상위 원소 (top): 스택의 top에 있는 데이터 반환
    def top(self):
        if self.is_empty():
            return None  # 스택이 비어있으면 None 반환
        return self.head.data  # top에 있는 데이터 반환

    # 스택이 비어있는지 확인 (is_empty)
    def is_empty(self):
        return self.head is None  # head가 None이면 비어있다는 의미

    # 스택의 원소들 출력
    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()  # 줄바꿈

# 사용 예시
stack = Stack()
stack.push(10)  # 스택에 10 삽입
stack.push(20)  # 스택에 20 삽입
stack.push(30)  # 스택에 30 삽입

stack.show()  # 스택의 모든 원소 출력: 30 20 10

print("Pop:", stack.pop())  # 최상위 원소 30 제거
stack.show()  # 20 10 출력

print("Top:", stack.top())  # 현재 top 원소 20 출력
print("Is Empty?", stack.is_empty())  # 스택이 비어있는지 확인
