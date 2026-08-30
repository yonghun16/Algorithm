"""
------------------------------------------------------------
Sub    : [Programmers] 공원
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/340198
Level  : 1
Tag    : Python, Simulation
------------------------------------------------------------
Approach
- 돗자리 크기 리스트(mats)와 공원 배치도(park)를 입력받음.
- 돗자리를 큰 것부터 순서대로 시도.
- 각 크기마다 공원의 모든 시작 위치 (i, j)를 완전탐색.
- 해당 위치에서 size x size 정사각형 범위가 전부 "-1"이면
  그 크기를 바로 정답으로 반환 (큰 것부터 시도했으므로 첫 성공이 최댓값).
- 끝까지 깔 수 있는 위치가 없으면 -1 반환.
------------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Input
def get_input_data() -> tuple[list[int], list[list[str]]]:
    """
    첫 줄: 돗자리 한 변 길이들 (예: "5 3 2")
    다음 줄부터: 공원 배치도 (행 개수는 입력 끝까지 가변적으로 읽음)
    """
    mats: list[int] = list(map(int, input().split()))
    park: list[list[str]] = [
        line.split() for line in sys.stdin if line.strip()
    ]
    return mats, park


# ⚙️ Logic
def can_place(park: list[list[str]], i: int, j: int, size: int) -> bool:
    """(i, j)를 좌상단으로 하는 size x size 정사각형이 전부 빈 칸("-1")인지 확인"""
    return all(
        park[i + di][j + dj] == "-1"
        for di in range(size)
        for dj in range(size)
    )


def solution(mats: list[int], park: list[list[str]]) -> int:
    height: int = len(park)
    width: int = len(park[0])

    for size in sorted(mats, reverse=True):
        for i in range(height - size + 1):
            for j in range(width - size + 1):
                if can_place(park, i, j, size):
                    return size

    return -1


# 🚀 Run Program
if __name__ == "__main__":
    print(solution(*get_input_data()))
