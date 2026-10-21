# ------------------------------------------------------------
# Sub    : [JOL] 최대공약수,최소공배수
# Date   : 2026-10-21
# Link   : https://jungol.co.kr/problem/1002
# Level  : Bronze 3
# Tag    : Python, Math, 정수론, 유클리드
# ------------------------------------------------------------

import os
import sys

if os.path.exists("./input_test.txt"):
    sys.stdin = open("./input_test.txt", "r", encoding="utf-8")

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 📥 Input
def get_input_data() -> List[int]:
    N = int(input())
    nums = list(map(int, input().split()))
    return nums


# ⚙️ Logic
def get_gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    else:
        return get_gcd(b, a % b)


def get_lcm(a: int, b: int, gcd: int) -> int:
    return (a * b) // gcd


def solution(data: list) -> None:
    a = data[0]
    b = data[1]
    gcd = get_gcd(a, b)
    lcm = get_lcm(a, b, gcd)

    for i in range(2, len(data)):
        gcd = get_gcd(gcd, data[i])
        lcm = get_lcm(lcm, data[i], get_gcd(lcm, data[i]))

    print(gcd, lcm)


# 🚀 Run Program
if __name__ == "__main__":
    solution(get_input_data())
