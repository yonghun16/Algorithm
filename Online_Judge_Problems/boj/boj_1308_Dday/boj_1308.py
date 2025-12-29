"""
-----------------------------------------------------------
Sub    : [BOJ] Dday
Link   : https://www.acmicpc.net/problem/1308
Level  : 실버 5
Tag    : Python, 구현
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys
from datetime import date

if sys.platform == "linux":
    lines = sys.stdin.read().strip().split("\n")
else:
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")

input = iter(lines).__next__


def solve():
    # 입력 받기
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())

    # 1. "gg" 조건 판별 (1000년 이상 차이)
    # D-Day 연도가 (오늘 연도 + 1000)보다 크면 무조건 gg
    # 연도가 정확히 1000년 차이날 때, 월/일 비교가 필요함
    if y2 - y1 > 1000:
        print("gg")
        return
    elif y2 - y1 == 1000:
        if m2 > m1 or (m2 == m1 and d2 >= d1):
            print("gg")
            return

    # 2. 날짜 차이 계산
    d_day = date(y2, m2, d2)
    today = date(y1, m1, d1)

    diff = d_day - today
    print(f"D-{diff.days}")


solve()
