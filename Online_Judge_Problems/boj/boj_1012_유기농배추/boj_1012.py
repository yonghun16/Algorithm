"""
------------------------------------------------------------
Sub    : [BOJ] 유기농 배추
Link   : https://www.acmicpc.net/problem/1012
Level  : 실버 2
Tag    : Python, DFS
Memo
------------------------------------------------------------
"""

import sys

# [환경 설정]
TEST_MODE = True


# [입력 처리 함수]
def get_inputs():
    if TEST_MODE:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip("\n")
    else:
        for line in sys.stdin:
            yield line.rstrip("\n")


input_gen = get_inputs()


def input():
    return next(input_gen)


sys.setrecursionlimit(10**7)


# DFS 정의
def dfs(x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                dfs(nx, ny)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    result = 0

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                field[y][x] = 0
                dfs(x, y)
                result += 1

    print(result)
