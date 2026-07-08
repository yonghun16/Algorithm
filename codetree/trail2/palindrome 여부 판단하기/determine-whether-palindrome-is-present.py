import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Input
def get_input_data() -> str:
    word = input().strip()

    return word


# ⚙️ Logic
def solution(word: str) -> str:
    if word == word[::-1]:
        return "Yes"
    else:
        return "No"


# 🚀 Run Program
if __name__ == "__main__":
    print(solution(get_input_data()))