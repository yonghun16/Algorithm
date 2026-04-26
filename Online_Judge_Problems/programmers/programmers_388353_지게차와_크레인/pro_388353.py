"""
-----------------------------------------------------------
Sub    : [Programmers] 지게차와 크레인
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/388353
Level  : 2
Tag    : BFS, Simulation
-----------------------------------------------------------
Solution
1. 크레인 (요청 길이 2)
    해당 문자 전부 제거
2. 지게차 (요청 길이 1)
   - "외부와 연결된" 컨테이너만 제거
   - 외부 판정 방법
       - 빈 공간('.')을 기준으로 가장자리에서 BFS 수행
       - BFS로 퍼지면서 만난 target 컨테이너만 제거 가능
-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Get Input Data
def get_input_data():
    storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
    requests = ["A", "BB", "A"]
    return storage, requests


# ⚙️ Core Logic
def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    board = [list(row) for row in storage]

    #  지게차
    def remove_by_forklift(target):
        visited = [[False] * m for _ in range(n)]
        q = []  # deque 대신 list 사용

        removable = set()

        # 1️⃣ 테두리 탐색
        for i in range(n):
            for j in range(m):
                if i in (0, n - 1) or j in (0, m - 1):

                    if board[i][j] == ".":
                        q.append((i, j))
                        visited[i][j] = True

                    elif board[i][j] == target:
                        removable.add((i, j))

        # 2️⃣ BFS (list 기반)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            x, y = q.pop(0)  # 여기만 변경됨 (O(n))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if board[nx][ny] == ".":
                        q.append((nx, ny))

                    elif board[nx][ny] == target:
                        removable.add((nx, ny))

        # 3️⃣ 제거
        for x, y in removable:
            board[x][y] = "."

    # 요청 처리
    for req in requests:
        target = req[0]

        #  크레인
        if len(req) == 2:
            for i in range(n):
                for j in range(m):
                    if board[i][j] == target:
                        board[i][j] = "."

        #  지게차
        else:
            remove_by_forklift(target)

    # 남은 개수
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != ".":
                answer += 1

    return answer


# 🚀 Run
if __name__ == "__main__":
    storage, requests = get_input_data()
    print(solution(storage, requests))
