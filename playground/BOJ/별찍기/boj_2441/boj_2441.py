'''----------------------------------------------------
Sub  : [BOJ] 별찍기 - 4
Link : https://www.acmicpc.net/problem/2441
Level: 브론즈 3
Tag  : Python, 구현
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

N = int(input().strip())

# N부터 1까지 별을 출력
for i in range(N, 0, -1):
    print(' ' * (N-i), end='')
    print('*' * i)
