"""
-----------------------------------------------------------
Sub    : [BOJ] 에디터
Link   : https://www.acmicpc.net/problem/1406
Level  : Silver 2
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


# left stack, right stack definition
left_stack = []
right_stack = []

# input
left_stack = list(input())
m = int(input())

# process
for _ in range(m):
    command = input()

    if command[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())

    elif command[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())

    elif command[0] == "B":
        if left_stack:
            left_stack.pop()

    elif command[0] == "P":
        left_stack.append(command[2])

# output
print("".join(left_stack + right_stack[::-1]))
