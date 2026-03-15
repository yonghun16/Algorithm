"""
-----------------------------------------------------------
Sub    : [BOJ] 단어 뒤집기2
Link   : https://www.acmicpc.net/problem/17413
Level  : Silver 3
Tag    : Python, String, Stack
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
        for char in line.rstrip("\n"):
            yield char


tokens = get_input()


# stack 클래스
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# input & init
words_stack = Stack()
is_tag = False  # 현재 문자가 태그 안에 있는지 확인하는 플래그
result = []  # result array for print

# solve
while True:
    char = next(tokens, None)

    if char is None:
        while not words_stack.is_empty():
            result.append(words_stack.pop())
        break

    # 1. 태그의 시작인 경우
    if char == "<":
        # 태그 시작 전까지 쌓인 단어를 먼저 뒤집어서 출력
        while not words_stack.is_empty():
            result.append(words_stack.pop())
        is_tag = True
        result.append(char)

    # 2. 태그의 끝인 경우
    elif char == ">":
        is_tag = False
        result.append(char)

    # 3. 태그 내부인 경우
    elif is_tag:
        result.append(char)

    # 4. 태그 밖의 일반 문자인 경우
    else:
        # 공백을 만나면 단어가 끝난 것이므로 스택을 비움
        if char == " ":
            while not words_stack.is_empty():
                result.append(words_stack.pop())
            result.append(char)
        else:
            words_stack.push(char)

# print
print("".join(result))
