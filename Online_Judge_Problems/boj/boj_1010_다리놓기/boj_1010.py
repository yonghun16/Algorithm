"""
------------------------------------------------------------
Sub    : [BOJ] 다리 놓기
Link   : https://www.acmicpc.net/problem/1010
Level  : silver 5
Tag    : Python, math
Memo
------------------------------------------------------------
"""

import math

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(math.comb(M, N))
