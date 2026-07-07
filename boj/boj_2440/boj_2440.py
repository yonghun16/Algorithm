'''----------------------------------------------------
Sub  : [BOJ] 별찍기 - 3
Link : https://www.acmicpc.net/problem/2440
Level: 브론즈 4
Tag  : Python, 구현
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

N = int(input().strip())

# N부터 1까지 별을 출력
for i in range(N, 0, -1):
    print('*' * i)
