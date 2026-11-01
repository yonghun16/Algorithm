# ------------------------------------------------------------
# Sub    : [JOL] 소수와 합성수
# Date   : 2026-11-01
# Link   : https://jungol.co.kr/problem/2811
# Level  : Bronze 4
# Tag    : Python,
# ------------------------------------------------------------
# Approach
# - 10억을 담을 수 있는 자료형(32bit int)에 숫자로 입력하여 튜플에 저장
# - 로직 함수에 넘기고
# - 소수를 판별할 수 있는 함수(로직 함수에서 호출)
#   - 넘겨받은 수가 1이면 리턴 (1)
#   - 순환문 i=2 -> ixi <= n을 돌리고
#     - i가 input_data의 약수인지 판별 약수이면 리턴 (컴포지트 넘버)
#   - 리턴되지 않은 수도 리턴(프라임 넘버 )
# ------------------------------------------------------------

import math
import os
import sys

if os.path.exists("./input_test.txt"):
    sys.stdin = open("./input_test.txt", "r", encoding="utf-8")  # noqa: SIM115

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 📥 Input
def get_input_data() -> tuple:
    arr = tuple(map(int, input().split()))
    return arr


# ⚙️ Logic
def is_prime_number(item: int) -> int:
    if item == 1:
        return 2
    for i in range(2, math.isqrt(item) + 1):
        if item % i == 0:
            return 1
    return 0


def solution(data: tuple) -> list:
    answer = []

    for item in data:
        answer.append(is_prime_number(item))

    return answer


# 📤 Output
def print_result(result: list[int]) -> None:
    result_data = ["prime number", "composite number", "number one"]
    for i in result:
        print(result_data[i])


# 🚀 Run Program
if __name__ == "__main__":
    data = get_input_data()
    result = solution(data)
    print_result(result)
