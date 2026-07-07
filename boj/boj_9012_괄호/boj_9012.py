'''----------------------------------------------------
Sub  : [BOJ] 괄호
Link : https://www.acmicpc.net/problem/9012
Level: 실버 4
Tag  : Python, Stack
Memo
----------------------------------------------------'''

import sys

TEST_MODE = True

def get_inputs():
    if TEST_MODE:
        with open('input1.txt', 'r') as f:
            for line in f:
                yield line.rstrip('\n')
    else:
        for line in sys.stdin:
            yield line.rstrip('\n')

input_gen = get_inputs()

def input():
    return next(input_gen)

# input
N = int(input().strip())
answer = []

# processing
for _ in range(N):
    line = input().strip()
    stack = []

    for ch in line:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                print('NO')
                break
            stack.pop()
    else:
        if stack:
            answer.append('NO')
        else:
            answer.append('YES')

# print
print('\n'.join(answer))


