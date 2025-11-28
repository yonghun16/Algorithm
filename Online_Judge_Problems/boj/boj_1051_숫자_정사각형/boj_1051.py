"""
------------------------------------------------------------
Sub    : [BOJ] 숫자 정사각형
Link   : https://www.acmicpc.net/problem/1051
Level  : 실버 3
Tag    : Python, brute force
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


# 입력
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

max_size = 1  # 최소 정사각형 크기는 1

for i in range(N):
    for j in range(M):
        # 현재 좌표를 왼쪽 위 꼭짓점으로 잡음
        for k in range(i, N):
            for l in range(j, M):
                # k-i == l-j → 정사각형이 되기 위한 조건
                if k - i == l - j:
                    # 꼭짓점 비교
                    if board[i][j] == board[i][l] == board[k][j] == board[k][l]:
                        size = (k - i + 1) ** 2
                        if size > max_size:
                            max_size = size

print(max_size)
