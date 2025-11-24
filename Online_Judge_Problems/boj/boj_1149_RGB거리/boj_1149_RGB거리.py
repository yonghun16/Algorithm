"""
------------------------------------------------------------
Sub    : [BOJ] RGB거리
Link   : https://www.acmicpc.net/problem/1149
Level  : 실버 1
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


# 집의 수 N 입력
n = int(input())

# 각 집의 비용을 저장하는 리스트 (2차원 배열)
# costs[i][0]: 빨강, costs[i][1]: 초록, costs[i][2]: 파랑
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))

# 1번 집(인덱스 1)부터 N번 집(인덱스 N-1)까지 순회
for i in range(1, n):
    # i번째 집을 빨강으로 칠할 때: 이전 집은 초록 또는 파랑 중 싼 것 선택
    costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])

    # i번째 집을 초록으로 칠할 때: 이전 집은 빨강 또는 파랑 중 싼 것 선택
    costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])

    # i번째 집을 파랑으로 칠할 때: 이전 집은 빨강 또는 초록 중 싼 것 선택
    costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

# 마지막 집(N-1)의 누적 비용 중 가장 작은 값이 정답
print(min(costs[n - 1]))
