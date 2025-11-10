"""
------------------------------------------------------------
Sub    : [BOJ] 1, 2, 3 더하기
Link   : https://www.acmicpc.net/problem/9095
Level  : 실버 3
Tag    : Python, DP
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


# 1, 2, 3 더하기

T = int(input())  # 테스트 케이스 개수
dp = [0] * 12  # n은 11보다 작음 (1~11까지 사용)

# 기본값
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 점화식 이용해 미리 계산
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

# 테스트 케이스별 출력
for _ in range(T):
    n = int(input())
    print(dp[n])
