"""
-----------------------------------------------------------
Sub    : [BOJ] 단어 나누기
Link   : https://www.acmicpc.net/problem/1251
Level  : 실버 5
Tag    : Python, Brute Force
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


word = input().strip()
n = len(word)

best = "z" * 100  # 충분히 큰 문자열로 초기화

for i in range(1, n - 1):
    for j in range(i + 1, n):
        # 세 구간 나누기
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        # 각각 뒤집고 합치기
        candidate = a[::-1] + b[::-1] + c[::-1]

        # 사전순 비교
        if candidate < best:
            best = candidate

print(best)
