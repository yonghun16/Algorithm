class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        # 마지막 위치에 원소 삽입
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        # 마지막 원소 추출
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        # 마지막 원소 반환
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()
arr = [9, 7, 2, 5, 6, 4, 2]
for x in arr:
    stack.push(x)

while not stack.is_empty():
    print(stack.pop())
