import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Input
def get_input_data() -> tuple[int, int]:
    a, b = map(int, input().split())

    return a, b


# ⚙️ Logic
def solution(a: int, b: int) -> tuple[int, int]:
    if a > b:
        a += 25
        b *= 2
    else:
        a *=2
        b += 25
    return a, b


# 🚀 Run Program
if __name__ == "__main__":
    print(*solution(*get_input_data()))