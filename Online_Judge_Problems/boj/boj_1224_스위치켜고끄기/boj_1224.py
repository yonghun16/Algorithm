"""
-----------------------------------------------------------
Sub    : [BOJ] 스위치 켜고 끄기
Link   : https://www.acmicpc.net/problem/1224
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

# 스위치 개수
n = int(input())

# 스위치 상태 (0-indexed)
switches = list(map(int, input().split()))

# 학생 수
m = int(input())

for _ in range(m):
    gender, num = map(int, input().split())
    idx = num - 1  # 인덱스 보정

    # 남학생
    if gender == 1:
        for i in range(idx, n, num):
            switches[i] ^= 1  # 토글

    # 여학생
    else:
        left = right = idx

        while left >= 0 and right < n and switches[left] == switches[right]:
            left -= 1
            right += 1

        # 대칭이 깨지기 직전까지 토글
        for i in range(left + 1, right):
            switches[i] ^= 1

# 출력 (20개씩)
for i in range(n):
    print(switches[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
