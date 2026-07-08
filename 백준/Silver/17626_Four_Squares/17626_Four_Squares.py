"""
------------------------------------------------------------
Sub    : [BOJ] Four Squares
Link   : https://www.acmicpc.net/problem/17626
Level  : 실버 3
Tag    : Python, DP
Memo
------------------------------------------------------------
"""

import sys
import math

# [환경 설정]
TEST_MODE = False


# [입력 처리 함수]
def get_inputs():
    # 로컬 테스트 (input.txt 파일 읽기)
    if TEST_MODE:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip("\n")
    else:
        # 제출 환경 (표준 입력)
        for line in sys.stdin:
            yield line.rstrip("\n")


input_gen = get_inputs()


def input():
    return next(input_gen)


n = int(input())

# 1. 하나의 제곱수로 표현 가능?
if int(math.isqrt(n)) ** 2 == n:
    print(1)
    exit()

# 2. 두 개의 제곱수로 표현 가능?
for i in range(1, int(math.isqrt(n)) + 1):
    if int(math.isqrt(n - i * i)) ** 2 == n - i * i:
        print(2)
        exit()

# 3. 세 개의 제곱수로 표현 가능?
#    라그랑주에 따라 4는 마지막 경우라 굳이 DP 불필요
for i in range(1, int(math.isqrt(n)) + 1):
    for j in range(1, int(math.isqrt(n - i * i)) + 1):
        if int(math.isqrt(n - i * i - j * j)) ** 2 == n - i * i - j * j:
            print(3)
            exit()

# 4. 나머지는 무조건 4
print(4)
