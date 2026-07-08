"""
-----------------------------------------------------------
Sub    : [BOJ] 학생 번호
Link   : https://www.acmicpc.net/problem/1235
Level  : 실버 4
Tag    : Python, 구현
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

if sys.platform == "linux":
    lines = sys.stdin.read().strip().split("\n")
else:
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")

input = iter(lines).__next__


N = int(input())
students = [input().strip() for _ in range(N)]

length = len(students[0])

for k in range(1, length + 1):
    seen = set()
    for s in students:
        seen.add(s[-k:])

    if len(seen) == N:
        print(k)
        break
