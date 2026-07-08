import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Input
def get_input_data() -> tuple[int, list[int]]:
    n = int(input().strip())
    numbers = list(map(int, input().split()))

    return n, numbers


# ⚙️ Logic
def solution(n: int, numbers: list[int]) -> tuple[int, list[int]]:
    answer = []
    for number in numbers:
        if(number % 2 == 0):
            answer.append(number // 2)
        else:
            answer.append(number)

    return answer


# 🚀 Run Program
if __name__ == "__main__":
    n, numbers = get_input_data()
    print(*solution(n, numbers))