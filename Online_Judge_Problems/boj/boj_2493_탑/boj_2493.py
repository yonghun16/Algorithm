"""
-----------------------------------------------------------
Sub    : [BOJ] 탑
Link   : https://www.acmicpc.net/problem/2493
Level  : Gold 5
Tag    : Python, Stack
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")
if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")
else:
    input = sys.stdin.readline


# Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# Input & Init
stack = Stack()
N = int(input())
towers = list(map(int, input().split()))
answer = []

# Solve
for i in range(N):
    current_height = towers[i]

    while not stack.is_empty():
        if towers[stack.peek()] < current_height:
            stack.pop()
        else:
            break

    if stack.is_empty():
        answer.append(0)
    else:
        answer.append(stack.peek() + 1)

    stack.push(i)


# Print
print(*(answer))
