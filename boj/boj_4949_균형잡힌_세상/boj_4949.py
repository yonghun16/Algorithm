'''----------------------------------------------------
Sub  : [BOJ] 균현잡힌 세상
Link : https://www.acmicpc.net/problem/4949
Level: 실버 4
Tag  : Python, Stack
Memo
----------------------------------------------------'''

import sys

TEST_MODE = True

def get_inputs():
    if TEST_MODE:
        with open('input.txt', 'r') as f:
            for line in f:
                yield line.rstrip('\n')
    else:
        for line in sys.stdin:
            yield line.rstrip('\n')

input_gen = get_inputs()

def input():
    return next(input_gen)


def balanced(line):
    stack = []
    pairs = {
        ')': '(', 
        ']': '['
    }
    for ch in line:
        if ch in '([':
            stack.append(ch)
        elif ch in ')]':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack   # 스택이 전부 비워져 있으면 True 반환


while True:
    line = input()
    if line == '.':  # 종료 조건
        break
    print('yes' if balanced(line) else 'no')
