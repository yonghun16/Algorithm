"""
-----------------------------------------------------------
Sub    : [BOJ] Prime Number
Link   : https://www.acmicpc.net/problem/1312
Level  : Silver 4
Tag    : Python, math
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

# 입력 처리 부분
if sys.platform == "linux":
    lines = sys.stdin.read().strip().split("\n")
else:
    # 로컬 환경에서 input.txt 파일을 사용할 경우
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.read().strip().split("\n")
    else:
        # 파일이 없으면 직접 입력을 받도록 예외 처리
        lines = [sys.stdin.readline()]

input_iter = iter(lines)


def get_input():
    return next(input_iter)


# 메인 로직
def solve():
    try:
        line = get_input()
        A, B, N = map(int, line.split())

        # 1. 먼저 정수 부분을 떼어내고 나머지만 남깁니다.
        remainder = A % B

        result = 0
        # 2. N번 반복하며 소수점 아래 숫자를 하나씩 구합니다.
        for _ in range(N):
            remainder *= 10
            result = remainder // B  # 이번 단계의 소수점 자리 숫자
            remainder %= B  # 다음 단계를 위한 나머지

        print(result)

    except StopIteration:
        pass


if __name__ == "__main__":
    solve()
