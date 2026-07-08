import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")

if os.path.exists(file_path):
    f = open(file_path, "r", encoding="utf-8")
    input = f.readline
else:
    input = sys.stdin.readline
