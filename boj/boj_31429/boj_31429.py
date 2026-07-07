'''
----------------------------------------------
Sub : [BOJ] SUAPC 2023 Summer
Link: https://www.acmicpc.net/problem/31429
Tag : Python, 
Memo
----------------------------------------------
'''

score_board = [
    [12, 1600],
    [11, 894],
    [11, 1327],
    [10, 1311],
    [9, 1004],
    [9, 1178],
    [9, 1357],
    [8, 837],
    [7, 1055],
    [6, 556],
    [6, 773],
]

n = int(input().strip())

print(score_board[n-1][0], score_board[n-1][1])
