"""
-----------------------------------------------------------
Sub    : [Programmers] 택배 상자 꺼내기
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/389478
Level  : 1
Tag    : Python,
-----------------------------------------------------------
Solution
1. '타겟 상자'와 '마지막 상자'의 (행, 열) 위치를 각각 계산
2. 꼭대기 바로 전 층까지 '확실하게 쌓여 있는' 상자 개수 확보
3. 맨 꼭대기 층(last_row)의 '동일한 열(col)'에 위치할 '꼭대기 상자 번호' 연산
    : 짝수 층: 왼쪽 -> 오른쪽 방향 역산
    : 홀수 층: 오른쪽 -> 왼쪽 방향 역산
4. 역산한 '꼭대기 상자 번호'가 실제 존재하는 상자(<= n)인지 검증
    : 존재한다면 맨 꼭대기 상자까지 포함하여 카운트 증가
5. 카운트된 상자 개수 반환 및 출력
-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Get Input Data
def get_input_data():
    n, w, num = map(int, input().split())
    return n, w, num


# 위치 계산 보조 함수
def get_coords(num, w):
    # 상자 번호 num이 몇 번째 층(row), 몇 번째 열(col)에 있는지 구하는 함수 (0-index 기반)
    row = (num - 1) // w
    remainder = (num - 1) % w

    if row % 2 == 0:
        col = remainder  # 짝수 층: 왼쪽 -> 오른쪽
    else:
        col = w - 1 - remainder  # 홀수 층: 오른쪽 -> 왼쪽

    return row, col


# ⚙️ Core Logic
def solution(n, w, num):
    row, col = get_coords(num, w)
    last_row, last_col = get_coords(n, w)

    # 꼭대기 바로 전 층까지 확실하게 존재하는 상자의 개수
    answer = last_row - row

    # 맨 꼭대기 층(last_row)의 같은 열(col)에 상자가 있는지 확인
    if last_row % 2 == 0:
        top_box_num = last_row * w + col + 1
    else:
        top_box_num = last_row * w + (w - 1 - col) + 1

    # 꼭대기 층에 있는 상자 번호가 전체 상자 개수 n 이하라면 실재하는 상자임
    if top_box_num <= n:
        answer += 1

    return answer


# 🚀 Run Program
if __name__ == "__main__":
    n, w, num = get_input_data()
    print(solution(n, w, num))
