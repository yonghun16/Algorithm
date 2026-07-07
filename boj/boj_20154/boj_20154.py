"""
-----------------------------------------------------------
Sub    : [BOJ] 이 구역의 승자는 누구야?
Link   : https://www.acmicpc.net/problem/20154
Level  : 브론즈 1
Tag    : Python, 구현
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

if sys.platform == "linux":
    lines = sys.stdin.read().strip().split("\n")
else:
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")

input = iter(lines).__next__

S = input().strip()

# 알파벳 획수 테이블
stroke = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 2,
    "E": 3,
    "F": 3,
    "G": 3,
    "H": 3,
    "I": 1,
    "J": 1,
    "K": 3,
    "L": 1,
    "M": 3,
    "N": 3,
    "O": 1,
    "P": 2,
    "Q": 2,
    "R": 2,
    "S": 1,
    "T": 2,
    "U": 1,
    "V": 1,
    "W": 2,
    "X": 2,
    "Y": 2,
    "Z": 1,
}

total = 0
for ch in S:
    total += stroke[ch]

if total % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
