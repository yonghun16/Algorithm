"""
-----------------------------------------------------------
Sub    : [BOJ] 오큰수
Link   : https://www.acmicpc.net/problem/17298
Level  : Gold 4
Tag    : Python, Stack
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    f = open(file_path, "r", encoding="utf-8")
    input = f.readline
else:
    input = sys.stdin.readline


# Stack 클래스
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


# input
N = int(input())
M = list(map(int, input().split()))

answer = [-1] * N
stack = Stack()

# solve
for i in range(N):
    while not stack.is_empty() and M[stack.peek()] < M[i]:
        index = stack.pop()
        answer[index] = M[i]

    stack.push(i)

# output
sys.stdout.write(" ".join(map(str, answer)))
