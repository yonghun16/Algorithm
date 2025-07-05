'''----------------------------------------------------
Sub  : [BOJ] 별찍기 - 6
Link : https://www.acmicpc.net/problem/2443
Level: 브론즈 3
Tag  : Python, 구현
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (i * 2 - 1))
