'''----------------------------------------------------
Sub  : [BOJ] 별찍기 - 5
Link : https://www.acmicpc.net/problem/2442
Level: 브론즈 3
Tag  : Python, 구현
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    print(" " * (n - i - 1) + "*" * (i * 2 + 1))
