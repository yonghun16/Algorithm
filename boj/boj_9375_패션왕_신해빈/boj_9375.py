"""
------------------------------------------------------------
Sub    : [BOJ] 패션왕 신해빈
Link   : https://www.acmicpc.net/problem/9375
Level  : 실버 3
Tag    : Python, math
Memo
------------------------------------------------------------
"""

import sys
from collections import defaultdict

# [환경 설정]
TEST_MODE = True


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


t = int(input().rstrip())  # 테스트 케이스 개수

for _ in range(t):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        name, kind = input().split()
        clothes[kind] += 1  # 종류별 개수 세기

    result = 1
    for kind in clothes:
        result *= clothes[kind] + 1  # 입지 않는 경우 포함

    print(result - 1)  # 알몸 제외
