"""
------------------------------------------------------------
Sub    : [BOJ] 1로 만들기
Link   : https://www.acmicpc.net/problem/1463
Level  : 실버3
Tag    : Python, DP
Memo
------------------------------------------------------------
"""

import sys

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


N = int(input().rstrip())

dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 기본적으로 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
