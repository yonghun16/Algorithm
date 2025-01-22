'''---------------------------------------------
Sub  : [BOJ] 체스판 다시 칠하기
Link : https://www.acmicpc.net/problem/1018
Level: 실버 4
Tag  : Python, 부루트포스
Memo
---------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력
# n = 체스판의 세로의 길이, m = 체스판의 가로의 길이
n, m = map (int, input().strip().split())
board = []

for i in range(n):
    board.append(input().strip())

result = 64

for start_x in range(n-7):
    for start_y in range(m-7):
        blackCase = 0 
        whiteCase = 0 
        for x in range(8):
            for y in range(8):
                if (x + y ) % 2:             # (0,0)과 같은 격자 칸
                    if board[start_x+x][start_y+y] == 'W':
                        blackCase += 1       # (0,0)과 같은 격자를 검정
                    else:
                        whiteCase += 1       # (0,0)을 같은 격자를 하양
                else:                        # 다른 격자 칸 
                    if board[start_x+x][start_y+y] == 'B':
                        blackCase += 1
                    else:
                        whiteCase += 1
        result = min(result, blackCase, whiteCase)

print(result)
