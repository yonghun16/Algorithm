"""
------------------------------------------------------------
Sub    : [Programmers] 지폐 접기_v2
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/340199
Level  : 1
Tag    : Python, Simulation
------------------------------------------------------------
Approach
- 지갑(wallet)과 지폐(bill)의 가로/세로 길이를 각각 "긴 변, 짧은 변" 순서로 정렬해
  비교 기준을 통일한다.
- 지폐가 지갑보다 큰 동안(가로 또는 세로가 지갑을 초과하는 동안) 반으로 접는다.
  - 접을 때마다 긴 변(bx)을 절반으로 줄인다.
  - 절반으로 줄인 뒤에는 긴 변/짧은 변 관계가 뒤바뀔 수 있으므로 다시 정렬해준다.
- 지폐의 가로·세로가 모두 지갑의 가로·세로 이하가 될 때까지 접은 횟수(answer)를 반환한다.
------------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Input
def get_input_data() -> tuple[list[int], list[int]]:
    wallet: list[int] = list(map(int, input().split()))
    bill: list[int] = list(map(int, input().split()))

    return wallet, bill


# ⚙️ Logic
def solution(wallet: list[int], bill: list[int]) -> int:
    w: list[int] = sorted(wallet, reverse=True)
    b: list[int] = sorted(bill, reverse=True)

    answer: int = 0
    while w < b:
        answer += 1
        b[0] //= 2
        b.sort(reverse=True)

    return answer


# 🚀 Run Program
if __name__ == "__main__":
    print(solution(*get_input_data()))
