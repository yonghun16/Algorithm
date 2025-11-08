"""
------------------------------------------------------------
Sub    : [BOJ] 바이러스
Link   : https://www.acmicpc.net/problem/2606
Level  : 실버 3
Tag    : Python, DFS
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


# 컴퓨터 수
n = int(input().rstrip())
# 연결된 쌍의 수
m = int(input().rstrip())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

# 방문 여부 리스트
visited = [False] * (n + 1)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


# 1번 컴퓨터부터 탐색 시작
dfs(1)

# 1번 제외한 감염된 컴퓨터 수 출력
print(visited.count(True) - 1)
