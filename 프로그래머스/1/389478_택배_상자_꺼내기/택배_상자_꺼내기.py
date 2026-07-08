"""
_-----------------------------------------------------------
Sub    : [Programmers] 택배 상자 꺼내기
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/389478
Level  : 1
Tag    : Python, Math
------------------------------------------------------------
Approach
- 타겟 상자와 마지막 상자의 (row, col) 좌표를 계산한다.
- 타겟 상자 위에 반드시 존재하는 상자의 개수를 계산한다.
- 마지막 층의 같은 열에 상자가 실제 존재하는지 확인한다.
------------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Input
def get_input_data() -> tuple[int, int, int]:
    n, w, num = map(int, input().split())
    return n, w, num


# ⚙️ Logic
def get_coords(num: int, w: int) -> tuple[int, int]:
    """
    상자 번호를 지그재그 적재 기준의 (row, col) 좌표로 변환한다.

    Args:
        num: 상자 번호 (1-indexed)
        w: 한 줄에 배치되는 상자 개수

    Returns:
        상자의 (row, col) 좌표 (0-indexed)
    """

    row = (num - 1) // w
    remainder = (num - 1) % w

    if row % 2 == 0:
        col = remainder
    else:
        col = w - 1 - remainder

    return row, col


def solution(n: int, w: int, num: int) -> int:
    """
    타겟 상자를 꺼내기 위해 제거해야 하는 상자의 개수를 계산한다.

    Args:
        n: 전체 상자 개수
        w: 한 줄에 배치되는 상자 개수
        num: 꺼낼 상자 번호

    Returns:
        제거해야 하는 상자의 개수
    """

    row, col = get_coords(num, w)
    last_row, _ = get_coords(n, w)

    # 꼭대기 바로 전 층까지는 반드시 상자가 존재한다.
    answer = last_row - row

    if last_row % 2 == 0:
        top_box_num = last_row * w + col + 1
    else:
        top_box_num = last_row * w + (w - 1 - col) + 1

    # 가장 윗층의 같은 열에도 상자가 존재하는 경우
    if top_box_num <= n:
        answer += 1

    return answer


# 🚀 Run Program
if __name__ == "__main__":
    n, w, num = get_input_data()
    print(solution(n, w, num))
