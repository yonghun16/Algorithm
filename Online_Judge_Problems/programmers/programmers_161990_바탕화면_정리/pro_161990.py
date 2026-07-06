"""
-----------------------------------------------------------
Sub    : [Programmers] 바탕화면 정리
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/161990
Level  : 1
Tag    : Python,
-----------------------------------------------------------
Solution

-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    sys.stdin = open(file_path, "r", encoding="utf-8")


# 📥 Get Input Data
def get_input_data():
    pass


# ⚙️ Core Logic
def solution():
    pass


# 🚀 Run Program
if __name__ == "__main__":
    get_input_data()
    solution()
