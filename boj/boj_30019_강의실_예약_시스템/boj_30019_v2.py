'''---------------------------------------------
Sub  : [BOJ] 강의실 예약 시스템
Link : https://www.acmicpc.net/problem/30019
Level: 브론즈 2
Tag  : Python, 구현, 그리디
Memo
---------------------------------------------'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

room = [0] * n

for i in range(m):

    k,s,e = map(int, input().split())
    
    if room[k -1] <= s:
        room[k -1] = e
        print('YES')
    else:
        print('NO')
