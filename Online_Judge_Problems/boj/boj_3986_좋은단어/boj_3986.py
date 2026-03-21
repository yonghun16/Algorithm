"""
-----------------------------------------------------------
Sub    : [BOJ] 좋은 단어
Link   : https://www.acmicpc.net/problem/3986
Level  : 실버 3
Tag    : Python, Stack
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys


def get_input():
    file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")
    if os.path.exists(file_path):
        f = open(file_path, "r", encoding="utf-8")
    else:
        f = sys.stdin

    for line in f:
        for char in line.split():
            yield char


tokens = get_input()


def input():
    return next(tokens)


# input & init
n = int(input())
answer = 0

# solve
for _ in range(n):
    word = input()
    stack = []

    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        answer += 1

# print
print(answer)
