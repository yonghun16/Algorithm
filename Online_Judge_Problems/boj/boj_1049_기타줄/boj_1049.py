"""
------------------------------------------------------------
Sub    : [BOJ] 기타줄
Link   : https://www.acmicpc.net/problem/1049
Level  : 실버 4
Tag    : Python, greedy
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

pack_min = 10**9
single_min = 10**9

for _ in range(M):
    pack, single = map(int, input().split())
    pack_min = min(pack_min, pack)
    single_min = min(single_min, single)

# 경우 1: 전부 패키지로만
case1 = pack_min * ((N + 5) // 6)

# 경우 2: 패키지 + 나머지는 낱개
case2 = pack_min * (N // 6) + single_min * (N % 6)

# 경우 3: 낱개로만
case3 = single_min * N

print(min(case1, case2, case3))
