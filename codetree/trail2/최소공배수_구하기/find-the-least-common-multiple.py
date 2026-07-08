import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Get Input Data
def get_input_data():
    n, m = map(int, input().split())
    return n, m


# ⚙️ Core Logic
def solution(n, m):
    left_number = n
    right_number = m

    while left_number != right_number:
        if left_number > right_number:
            right_number += m
        elif left_number < right_number:
            left_number += n

    print(left_number)


# 🚀 Run Program
if __name__ == "__main__":
    n, m = get_input_data()
    solution(n, m)
