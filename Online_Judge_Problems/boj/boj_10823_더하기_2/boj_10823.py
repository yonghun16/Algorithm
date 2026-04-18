"""
-----------------------------------------------------------
Sub    : [BOJ] 더하기 2 (10823)
Link   : https://www.acmicpc.net/problem/10823
Level  : Bronze 1
Tag    : Python, String, Parsing
-----------------------------------------------------------
Solution
1. 입력이 여러 줄에 걸쳐 들어오므로 sys.stdin.read()를 사용하여 전체를 하나의 문자열로 읽습니다.
2. 줄바꿈 문('\n')을 모두 제거하여 하나의 연속된 숫자/콤마 문자열을 만듭니다.
3. 콤마(',')를 기준으로 split하여 숫자 리스트를 생성합니다.
4. 각 숫자를 정수형으로 변환하여 합계를 구합니다.
-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")
if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")

# 전역 변수로 데이터 관리
full_string = ""


# 📥 Get Input Data
def get_input_data():
    # 모든 입력을 하나로 읽고 줄바꿈을 제거합니다.
    # 입력을 끝까지 읽어야 하므로 read()를 사용합니다.
    full_string = sys.stdin.read().replace("\n", "").replace(" ", "")

    return full_string


# ⚙️ Core Logic
def solution(full_string):
    if not full_string:
        return

    # 콤마를 기준으로 나누어 정수로 변환 후 합산
    numbers = full_string.split(",")
    total_sum = sum(int(num) for num in numbers if num)

    print(total_sum)


# 🚀 Run Program
if __name__ == "__main__":
    full_string = get_input_data()
    solution(full_string)
