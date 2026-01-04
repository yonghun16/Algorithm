"""
-----------------------------------------------------------
Sub    : [BOJ] 효령과 새 모니터
Link   : https://www.acmicpc.net/problem/20949
Level  : 실버 5
Tag    : Python, sort
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

if sys.platform == "linux":
    lines = sys.stdin.read().splitlines()
else:
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
    else:
        lines = []

input = iter(lines).__next__


def solve():
    try:
        N = int(input())
        monitors = []
        for i in range(1, N + 1):
            W, H = map(int, input().split())
            monitors.append((W**2 + H**2, i))

        # 정렬 및 출력 로직...
        monitors.sort(key=lambda x: (-x[0], x[1]))
        print("\n".join(str(m[1]) for m in monitors))

    except (StopIteration, ValueError):
        # 데이터가 없거나 입력이 끝났을 때 에러 방지
        pass


if __name__ == "__main__":
    solve()
