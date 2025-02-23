class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        # 스텍에 원소 추가
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        # 스텍에서 원소 추출
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        # 스텍의 최상단 원소 반환
        return self.stack[-1]

    def display(self):
        # 스텍 출력
        print("\n   ↓ 스택의 최상단 ");
        print("│     │");
        for i in range(len(self.stack) - 1, -1, -1):
            print("│%4d │" % self.stack[i]);
        print("└─────┘");

    def is_empty(self):
        return len(self.stack) == 0


print("───────────────────────────────\n");
print("   List을 이용한 Stack의 구현  \n");
print("───────────────────────────────\n");
print();

stack = Stack()

while(True):
    menu = int(input("Push(1), Pop(2), Peek(3), len(4), EXIT(0) : "))

    if menu == 1:
        stack.push(int(input("Input Data : ")))
        stack.display()
    elif menu == 2:
        print("Pop Data : ", stack.pop())
        stack.display()
    elif menu == 3:
        print("Peek Data : ", stack.peek())
        print()
    elif menu == 4:
        print("Stack Length : ", len(stack.stack))
        print()
    elif menu == 0:
        break
    else:
        print("Wrong Input\n")
        continue
