"""
------------------------------------------------------------
Sub    : [BOJ] DFS와 BFS
Link   : https://www.acmicpc.net/problem/1260
Level  : 실버 2
Tag    : Python, DFS, BFS
Memo
------------------------------------------------------------
"""

import sys
from collections import deque

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


N, M, V = map(int, input().split())

# 인접 리스트 생성
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문해야 하므로 정렬
for i in range(1, N + 1):
    graph[i].sort()


# DFS 구현 (재귀)
def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, visited)


# BFS 구현
def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)


# 실행
visited = [False] * (N + 1)
dfs(V, visited)
print()
bfs(V)
