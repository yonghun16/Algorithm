"""
-----------------------------------------------------------
Sub    : [Programmers] 덧칠하기
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/161989
Level  : Lv.1
Tag    : Greedy
-----------------------------------------------------------
Solution

가장 왼쪽의 미칠 구역부터 시작해서
길이 m만큼 한 번에 칠하며 커버 범위를 갱신한다.
-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Get Input Data
def get_input_data():
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    section = list(map(int, input().strip().split(",")))
    return n, m, section


# ⚙️ Core Logic
def solution(n, m, section):
    answer = 0
    painted_end = 0  # 현재까지 칠해진 끝 위치

    for s in section:
        # 아직 안 칠해진 구역이면
        if s > painted_end:
            answer += 1
            painted_end = s + m - 1  # 이번에 칠한 범위

    return answer


# 🚀 Run Program
if __name__ == "__main__":
    n, m, section = get_input_data()
    print(solution(n, m, section))
