"""
-----------------------------------------------------------
Sub    : [BOJ] 수들의합
Link   : https://www.acmicpc.net/problem/2003
Level  : 실버 4
Tag    : Python, math, brute force
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
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    count = 0
    current_sum = 0
    start = 0
    end = 0

    # end 포인터를 이동시키며 반복
    while True:
        if current_sum >= m:
            # 합이 M보다 크거나 같으면 start를 이동시켜 합을 줄임
            current_sum -= a[start]
            start += 1
        elif end == n:
            # 합이 M보다 작은데 end가 끝에 도달했다면 더 이상 M을 만들 수 없음
            break
        else:
            # 합이 M보다 작으면 end를 이동시켜 합을 키움
            current_sum += a[end]
            end += 1

        # 조작 후 합이 M과 같다면 카운트 증가
        if current_sum == m:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()
