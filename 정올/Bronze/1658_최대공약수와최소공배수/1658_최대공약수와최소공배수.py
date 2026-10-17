# ------------------------------------------------------------
# Sub    : [JOL] 최대공약수와최소공배수
# Date   : 2026-10-17
# Link   : https://jungol.co.kr/problem/1658
# Level  : Bronze 3
# Tag    : Python, Math
# ------------------------------------------------------------
# Approach
# A, B 입력
# 유클리드 호제법을 사용하여 GCM 구함.
# LCM = A * B // GCM 을 통해 구함.
# ------------------------------------------------------------


import os
import sys

if os.path.exists("./input_test.txt"):
    sys.stdin = open("./input_test.txt", "r", encoding="utf-8")

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 📥 Input
def get_input_data() -> tuple:
    A, B = map(int, input().split())
    return (A, B)


# ⚙️ Logic
def get_gcd(a, b):
    if a % b == 0:
        return b
    else:
        return get_gcd(b, a % b)


def solution(data: tuple) -> None:
    a = data[0]
    b = data[1]
    gcd = get_gcd(a, b)

    print(gcd)
    print((a * b) // gcd)


# 🚀 Run Program
if __name__ == "__main__":
    solution(get_input_data())
