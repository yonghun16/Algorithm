"""
-----------------------------------------------------------
Sub    : [BOJ] 팔 (1105)
Link   : https://www.acmicpc.net/problem/1105
Level  : Silver 1
Tag    : Python, Greedy, Math
-----------------------------------------------------------
Solution
1. L과 R의 자릿수가 다르면 8이 하나도 없는 숫자(0개)를 반드시 만들 수 있습니다.
   (예: 88 ~ 100 사이엔 90, 99 등이 있음)
2. 자릿수가 같다면, 가장 큰 자릿수(왼쪽)부터 하나씩 비교합니다.
3. 두 숫자가 '8'로 동일하면 카운트를 증가시킵니다.
4. 두 숫자가 달라지는 순간, 그 뒤로는 숫자를 조정해 8이 안 나오게 할 수 있으므로 종료합니다.
-----------------------------------------------------------
"""

import os
import sys

# 파일 입력 설정 (로컬 테스트용)
file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")
if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")

# 전역 변수
L_str, R_str = "", ""


# 📥 Get Input Data
def get_input_data():
    global L_str, R_str
    # readline()을 사용하여 첫 번째 줄만 깔끔하게 가져옵니다.
    line = sys.stdin.readline().split()
    if len(line) == 2:
        L_str, R_str = line, line


# ⚙️ Core Logic
def solution():
    # 입력이 제대로 들어오지 않은 경우 방지
    if not L_str or not R_str:
        return

    # 1. 자릿수 길이가 다르면 사이의 숫자로 8을 피할 수 있음
    if len(L_str) != len(R_str):
        print(0)
        return

    # 2. 자릿수가 같을 때만 비교 시작
    count_eight = 0
    for i in range(len(L_str)):
        # 숫자가 같으면 그 숫자가 8인지 확인
        if L_str[i] == R_str[i]:
            if L_str[i] == "8":
                count_eight += 1
        else:
            break

    print(count_eight)


# 🚀 Run Program
if __name__ == "__main__":
    get_input_data()
    solution()
