"""
-----------------------------------------------------------
Sub    : [BOJ] 스택2
Link   : https://www.acmicpc.net/problem/28278
Level  : Silver 4
Tag    : Python, Stack
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
else:
    lines = sys.stdin.read().splitlines()

input = iter(lines).__next__


# 스택
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.items:
            return -1
        return self.items.pop()

    def is_empty(self):
        return 1 if not self.items else 0

    def peek(self):
        if not self.items:
            return -1
        return self.items[-1]


# input
N = int(input())
stack = Stack()
results = []

# solve
for _ in range(N):
    command = input().split()
    if not command:
        continue

    cmd_type = command[0]

    if cmd_type == "1":
        stack.push(command[1])
    elif cmd_type == "2":
        results.append(str(stack.pop()))
    elif cmd_type == "3":
        results.append(str(len(stack.items)))
    elif cmd_type == "4":
        results.append(str(stack.is_empty()))
    elif cmd_type == "5":
        results.append(str(stack.peek()))

# print
sys.stdout.write("\n".join(results) + "\n")
