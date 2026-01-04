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
    # input
    N = int(input())
    monitors = []

    for i in range(1, N + 1):
        W, H = map(int, input().split())
        monitors.append((W**2 + H**2, i))

    # sort
    monitors.sort(key=lambda x: (-x[0], x[1]))

    # print
    print("\n".join(str(m[1]) for m in monitors))


if __name__ == "__main__":
    solve()
