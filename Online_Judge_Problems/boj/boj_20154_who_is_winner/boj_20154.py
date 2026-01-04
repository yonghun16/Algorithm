"""
-----------------------------------------------------------
Sub    : [BOJ] Who is Winner
Link   : https://www.acmicpc.net/problem/20154
Level  : bronze 1
Tag    : Python, implement
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
