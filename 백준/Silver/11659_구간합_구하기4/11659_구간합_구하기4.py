"""
------------------------------------------------------------
Sub    : [BOJ] 구간 합 구하기 4
Link   : https://www.acmicpc.net/problem/11659
Level  : Silver 3
Tag    : Python, sum
Memo
------------------------------------------------------------
"""

import sys

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


N, M = map(int, input().split())

# input of N
nums = list(map(int, input().split()))

# making to sum array
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + nums[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
