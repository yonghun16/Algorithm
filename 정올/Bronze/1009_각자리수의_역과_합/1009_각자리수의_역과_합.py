# ------------------------------------------------------------
# Sub    : [JOL] 각 자리수의 역과 합
# Date   : 2026-10-24
# Link   : https://jungol.co.kr/problem/1009
# Level  : Bronze 4
# Tag    : Python, Math
# ------------------------------------------------------------
# Approach
# 양의 정수를 입력받아 역수와 각 자리 숫자의 합을 출력
# 0이 입력되면 종료, 최대 10개까지 입력받음
# 역수: 문자열 슬라이싱으로 구현
# 자리수 합: 제너레이터 식과 sum() 사용
# ------------------------------------------------------------

import os
import sys

if os.path.exists("./input_test.txt"):
    sys.stdin = open("./input_test.txt", "r", encoding="utf-8")  # noqa: SIM115

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 📥 Input
def get_input_data() -> tuple:
    numbers = []
    for _ in range(10):
        num = int(input())
        if num == 0:
            break
        numbers.append(num)
    return (numbers,)


# ⚙️ Logic
def solution(data: tuple) -> list:
    answer = []
    numbers = data[0]

    for num in numbers:
        # 역수 구하기
        num_str = str(num)
        reversed_num = int(num_str[::-1])

        # 각 자리 숫자의 합 구하기
        digit_sum = sum(int(digit) for digit in num_str)

        # 정담 저장
        answer.append((reversed_num, digit_sum))

    # 정담 반환
    return answer


# 📤 Output
def print_result(result) -> None:
    for reversed_num, digit_sum in result:
        print(reversed_num, digit_sum)


# 🚀 Run Program
if __name__ == "__main__":
    data = get_input_data()
    result = solution(data)
    print_result(result)
