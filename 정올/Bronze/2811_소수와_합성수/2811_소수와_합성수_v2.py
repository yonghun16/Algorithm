import math
import os
import sys

if os.path.exists("./input_test.txt"):
    sys.stdin = open("./input_test.txt", "r", encoding="utf-8")  # noqa: SIM115

read_line = sys.stdin.readline


# 📥 Input
def get_input_data() -> list[int]:
    return list(map(int, read_line().split()))


# ⚙️ Logic
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def classify(n: int) -> str:
    if n == 1:
        return "number one"
    return "prime number" if is_prime(n) else "composite number"


def solution(data: list[int]) -> list[str]:
    return [classify(item) for item in data]


# 📤 Output
def print_result(result: list[str]) -> None:
    for line in result:
        print(line)


# 🚀 Run Program
if __name__ == "__main__":
    data = get_input_data()
    result = solution(data)
    print_result(result)
