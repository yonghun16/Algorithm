class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 가장 뒤에 노드 삽입
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드를 하나씩 출력
    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    # 특정 인덱스(index)의 노드 찾기 (예외 처리 추가)
    def search(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        node = self.head
        for _ in range(index):
            if node is None:
                raise IndexError("Index out of range")
            node = node.next
        if node is None:
            raise IndexError("Index out of range")
        return node

    # 특정 인덱스(index)에 노드 삽입 (예외 처리 추가)
    def insert(self, index, data):
        new = Node(data)
        if index == 0:
            new.next = self.head
            self.head = new
            return
        try:
            node = self.search(index - 1)
        except IndexError:
            print(f"Insert Error: Index {index} out of range")
            return
        new.next = node.next
        node.next = new

    # 특정 인덱스(index)의 노드 삭제 (예외 처리 추가)
    def remove(self, index):
        if self.head is None:
            print("Remove Error: List is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        try:
            front = self.search(index - 1)
            if front.next is None:
                raise IndexError("Index out of range")
        except IndexError:
            print(f"Remove Error: Index {index} out of range")
            return
        front.next = front.next.next


linked_list = LinkedList()
data_list = [3, 5, 9, 8, 5, 6, 1, 7]

for data in data_list:
    linked_list.append(data)

print("전체 노드 출력:", end=" ")
linked_list.show()

linked_list.insert(4, 4)
print("전체 노드 출력:", end=" ")
linked_list.show()

linked_list.remove(7)
print("전체 노드 출력:", end=" ")
linked_list.show()

linked_list.insert(7, 2)
print("전체 노드 출력:", end=" ")
linked_list.show()
