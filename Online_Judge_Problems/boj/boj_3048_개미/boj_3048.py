"""
-----------------------------------------------------------
Sub    : [BOJ] 개미
Link   : https://www.acmicpc.net/problem/3048
Level  : 실버 4
Tag    : Python, 구현
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

is_linux = sys.platform == "linux"
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

if not is_linux and os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
else:
    lines = sys.stdin.read().splitlines()

input = iter(lines).__next__


n1, n2 = map(int, input().split())
group1 = list(input())
group2 = list(input())
t = int(input())

state = [1] * n1 + [0] * n2

for _ in range(t):
    i = 0
    while i < len(state) - 1:
        # 1(오른쪽행)과 0(왼쪽행)이 마주치면 교환
        if state[i] == 1 and state[i+1] == 0:
            state[i], state[i+1] = state[i+1], state[i]
            i += 2
        else:
            i += 1

ans = []
ptr1 = n1 - 1
ptr2 = 0
for s in state:
    if s == 1:
        ans.append(group1[ptr1])
        ptr1 -= 1
    else:
        ans.append(group2[ptr2])
        ptr2 += 1

print("".join(ans))