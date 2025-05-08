'''----------------------------------------------------
Sub  : [BOJ] 스택
Link : https://www.acmicpc.net/problem/10828
Level: 실버 4
Tag  : Python, Stack
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 스택 생성
class Stack:
    # 스택 생성(List)
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    # 1. push: 정수 x를 스택에 넣는 연산이다.
    def push(self, x):
        self.stack.append(x)

    # 2. pop: 스택에서 가장위에 있는 정수를 빼고, 그 수를 출력한다.
    #         만약에 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop(self):
        if self.is_empty():
            return "-1"
        return self.stack.pop()

    # 3. size: 스택에 들어있는 정수의 개수를 출력한다.
    def size(self):
        return len(self.stack)

    # 4. empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    def empty(self):
        if self.is_empty():
            return "1"
        return "0"

    # 5. top: 스택의 가장 위에 있는 정수를 출력한다.
    #         만약 스택에 들어있는 정수가 없을 경우에는 -1을 출력한다.
    def peek(self):
        if self.is_empty():
            return "-1"
        return self.stack[-1]

# 입력 받기
n = int(input().strip())
commands = [list(input().strip().split()) for _ in range(n)]

# 스택 명령 처리
stack = Stack()
for _ in range(len(commands)):
    if commands[_][0] == "push":
        stack.push(commands[_][1])
    elif commands[_][0] == "pop":
        print(stack.pop())
    elif commands[_][0] == "size":
        print(stack.size())
    elif commands[_][0] == "empty":
        print(stack.empty())
    elif commands[_][0] == "top":
        print(stack.peek())
