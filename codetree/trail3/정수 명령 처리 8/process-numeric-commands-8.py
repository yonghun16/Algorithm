N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, num):
        new_node = Node(num)
        if self.head is None:          # 비어있을 때
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def push_back(self, num):
        new_node = Node(num)
        if self.tail is None:          # 비어있을 때
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_front(self):
        result = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:                          # 리스트가 다 비게 된 경우
            self.tail = None
        self.length -= 1
        return result

    def pop_back(self):
        result = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:                          # 리스트가 다 비게 된 경우
            self.head = None
        self.length -= 1
        return result

    def size(self):
        return self.length

    def empty(self):
        return 1 if self.length == 0 else 0

    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data


dll = DLL()
result = []

for cmd, val in zip(command, A):
    if cmd == "push_front":
        dll.push_front(val)
    elif cmd == "push_back":
        dll.push_back(val)
    elif cmd == "pop_front":
        result.append(dll.pop_front())
    elif cmd == "pop_back":
        result.append(dll.pop_back())
    elif cmd == "size":
        result.append(dll.size())
    elif cmd == "empty":
        result.append(dll.empty())
    elif cmd == "front":
        result.append(dll.front())
    elif cmd == "back":
        result.append(dll.back())

print('\n'.join(map(str, result)))