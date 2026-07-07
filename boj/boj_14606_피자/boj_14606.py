"""
-----------------------------------------------------------
Sub    : [BOJ] 피자 (Small)
Link   : https://www.acmicpc.net/problem/14606
Level  : Silver 5
Tag    : Python, implement
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

is_linux = sys.platform == "linux"
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

if not is_linux and os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
else:
    lines = sys.stdin.read().splitlines()

input = iter(lines).__next__

result = 0

# input
n = int(input())

# process
result = n * (n - 1) // 2

# output
print(result)
