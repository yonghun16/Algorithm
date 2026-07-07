"""
-----------------------------------------------------------
Sub    : [BOJ] 대출 요청
Link   : https://www.acmicpc.net/problem/16497
Level  : 브론즈 2
Tag    : Python
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys


def get_input():
    if not sys.stdin.isatty():
        f = sys.stdin
    else:
        file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")
        if os.path.exists(file_path):
            f = open(file_path, "r", encoding="utf-8")
        else:
            f = sys.stdin

    for line in f:
        for char in line.split():
            yield char


tokens = get_input()


def input_token():
    return next(tokens)


def solve():
    try:
        n_str = input_token()
        if not n_str:
            return
        n = int(n_str)

        requests = []
        for _ in range(n):
            s = int(input_token())
            e = int(input_token())
            requests.append((s, e))

        k = int(input_token())

        days = [0] * 32
        for s, e in requests:
            for i in range(s, e):
                days[i] += 1

        if max(days) > k:
            print(0)
        else:
            print(1)

    except (StopIteration, ValueError):
        pass


if __name__ == "__main__":
    solve()
