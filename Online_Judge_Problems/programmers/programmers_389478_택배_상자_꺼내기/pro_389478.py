"""
-----------------------------------------------------------
Sub    : [Programmers] 택배 상자 꺼내기
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/389478
Level  : 1
Tag    : Python,
-----------------------------------------------------------
Solution

-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Get Input Data
def get_input_data():
    global n, w, num
    # 파일이나 표준 입력으로부터 한 줄을 읽어 공백으로 분리합니다.
    line = sys.stdin.read().split()
    if line:
        n = int(line[0])
        w = int(line[1])
        num = int(line[2])
    return n, w, num


# ⚙️ 위치 계산 보조 함수
def get_coords(x, w_val):
    """상자 번호 x가 몇 번째 층(row), 몇 번째 열(col)에 있는지 구하는 함수 (0-index 기반)"""
    row = (x - 1) // w_val
    remainder = (x - 1) % w_val

    if row % 2 == 0:
        col = remainder  # 짝수 층: 왼쪽 -> 오른쪽
    else:
        col = w_val - 1 - remainder  # 홀수 층: 오른쪽 -> 왼쪽

    return row, col


# ⚙️ Core Logic
def solution(n, w, num):
    row, col = get_coords(num, w)

    answer = 0
    # 전체 상자 중 가장 높은 층을 구합니다.
    max_row = (n - 1) // w

    # 타겟 상자가 있는 층부터 가장 꼭대기 층까지 탐색
    for r in range(row, max_row + 1):
        # 현재 층(r)과 타겟 열(target_col)에 위치한 상자의 실제 번호를 역산
        if r % 2 == 0:
            current_num = r * w + col + 1
        else:
            current_num = r * w + (w - 1 - col) + 1

        # 역산한 상자 번호가 전체 상자 개수 n 이하 인지 확인
        if current_num <= n:
            answer += 1

    return answer


# 🚀 Run Program
if __name__ == "__main__":
    n, w, num = get_input_data()
    print(solution(n, w, num))
