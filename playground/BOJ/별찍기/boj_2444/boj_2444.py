'''----------------------------------------------------
Sub  : [BOJ] 별찍기 - 7
Link : https://www.acmicpc.net/problem/2444
Level: 브론즈 3
Tag  : Python, 구현
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n-1):
    print(" " * (n - i - 1) + "*" * (i * 2 + 1))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (i * 2 - 1))
