"""
------------------------------------------------------------
Sub    : [BOJ] 랜선 자르기
Link   : https://www.acmicpc.net/problem/1654
Level  : 실버 2
Tag    : Python, Binary search
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


# input
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

# 이분 탐색 범위: 1cm ~ 가장 긴 랜선 길이
left, right = 1, max(lines)
result = 0

while left <= right:
    mid = (left + right) // 2  # 자를 길이
    count = 0

    for line in lines:
        count += line // mid  # mid로 잘랐을 때 몇 개 나오는지

    if count >= N:
        # 만들 수 있는 개수가 충분 → mid를 늘려서 더 긴 길이 가능할지 확인
        result = mid
        left = mid + 1
    else:
        # 개수가 부족 → 길이를 줄여야 함
        right = mid - 1

print(result)
