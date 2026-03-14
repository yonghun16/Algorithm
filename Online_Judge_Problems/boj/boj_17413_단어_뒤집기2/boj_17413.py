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


# 단어를 뒤집기 위한 스택 선언
words_stack = Stack()
is_tag = False  # 현재 문자가 태그 안에 있는지 확인하는 플래그

# solve
while True:
    char = next(tokens, None)

    # 더 이상 읽을 문자가 없으면 루프 종료
    if char is None:
        while not words_stack.is_empty():
            print(words_stack.pop(), end="")
        break

    # 1. 태그의 시작인 경우
    if char == "<":
        # 태그 시작 전까지 쌓인 단어를 먼저 뒤집어서 출력
        while not words_stack.is_empty():
            print(words_stack.pop(), end="")
        is_tag = True
        print(char, end="")

    # 2. 태그의 끝인 경우
    elif char == ">":
        is_tag = False
        print(char, end="")

    # 3. 태그 내부인 경우
    elif is_tag:
        print(char, end="")

    # 4. 태그 밖의 일반 문자인 경우
    else:
        # 공백을 만나면 단어가 끝난 것이므로 스택을 비움
        if char == " ":
            while not words_stack.is_empty():
                print(words_stack.pop(), end="")
            print(char, end="")  # 공백은 그대로 출력
        else:
            words_stack.push(char)

print()
