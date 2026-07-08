"""
-----------------------------------------------------------
Sub    : [BOJ] 6174
Link   : https://www.acmicpc.net/problem/6174
Level  : silver 5
Tag    : Python, Math
-----------------------------------------------------------
Details
- "".join() : 리스트 안에 있는 문자열들을 하나로 이어 붙입니다.

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


# 카프리카 연산 함수
def get_kaprekar(n):
    digits = list(str(n).zfill(4))

    big = int("".join(sorted(digits, reverse=True)))
    small = int("".join(sorted(digits)))

    return big - small


def solve():
    # variable
    kaprekar = 6174
    result = []

    # input
    n = int(input())
    nums = []

    for _ in range(n):
        nums.append(int(input()))

    # logic
    for num in nums:
        count = 0
        current = num

        while current != kaprekar:
            current = get_kaprekar(current)
            count += 1

        result.append(count)

    # output
    print("\n".join(map(str, result)))


if __name__ == "__main__":
    solve()
