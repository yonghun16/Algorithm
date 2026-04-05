"""
-----------------------------------------------------------
Sub    : [Programmers] 문제 제목
Link   : https://school.programmers.co.kr/learn/courses/30/lessons/250125
Level  : 1
Tag    : Python,
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

file_path = os.path.join(os.path.dirname(__file__), "input_test.txt")
if os.path.exists(file_path):
    f = open(file_path, "r", encoding="utf-8")
else:
    f = sys.stdin

data = f.read().split()

n = 4
board = []
for i in range(n):
    board.append(data[i * n : (i + 1) * n])

h = int(data[n * n])
w = int(data[n * n + 1])


def solution(board, h, w):
    n_size = len(board)
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n_size and 0 <= w_check < n_size:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count


print(solution(board, h, w))
