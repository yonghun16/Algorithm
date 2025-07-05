'''---------------------------------------------
Sub  : [BOJ] 시계탑
Link : https://www.acmicpc.net/problem/31561
Level: B3
Tag  : Python, 수학
Memo
 - 
---------------------------------------------'''

import sys
input = sys.stdin.readline

M = int(input().strip())
result = 0.0

if 0 < M <= 30:
    result = M/2
elif 30 < M < 60:
    result = (30)/2 + (M-30)*3/2

print(round(result, 1))
