"""
------------------------------------------------------------
Sub    : [BOJ] 11727 2xn타일링 2
Link   : https://www.acmicpc.net/problem/11727
Level  : 실버 3
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


n = int(sys.stdin.readline().strip())
MOD = 10007

if n == 1:
    print(1)
    sys.exit(0)
if n == 2:
    print(3)
    sys.exit(0)

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD

print(dp[n] % MOD)
