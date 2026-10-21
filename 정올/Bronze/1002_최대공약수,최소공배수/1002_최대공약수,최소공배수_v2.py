# ------------------------------------------------------------
# Sub    : [JOL] 최대공약수,최소공배수
# Date   : 2026-10-21
# Link   : https://jungol.co.kr/problem/1002
# Level  : Bronze 3
# Tag    : Python, Math, 정수론, 유클리드
# ------------------------------------------------------------

import os
import sys
from functools import reduce

if os.path.exists("./input_test.txt"):
    sys.stdin = open("./input_test.txt", "r", encoding="utf-8")

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 📥 Input
def get_input_data() -> List[int]:
    """입력 데이터를 받아서 정수 리스트로 반환합니다."""
    n = int(input())
    return list(map(int, input().split()))


# ⚙️ Logic
def gcd(a: int, b: int) -> int:
    """유클리드 호제법을 사용하여 최대공약수를 구합니다.

    Args:
        a: 첫 번째 수
        b: 두 번째 수

    Returns:
        a와 b의 최대공약수
    """
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """두 수의 최소공배수를 구합니다.

    Args:
        a: 첫 번째 수
        b: 두 번째 수

    Returns:
        a와 b의 최소공배수
    """
    return (a * b) // gcd(a, b)


def solution(data: List[int]) -> None:
    """여러 수의 최대공약수와 최소공배수를 구해서 출력합니다."""
    result_gcd = reduce(gcd, data)
    result_lcm = reduce(lcm, data)

    print(result_gcd, result_lcm)


# 🚀 Run Program
if __name__ == "__main__":
    solution(get_input_data())
