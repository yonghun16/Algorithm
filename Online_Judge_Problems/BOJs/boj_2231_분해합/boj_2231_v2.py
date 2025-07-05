'''----------------------------------------------------
Sub : [BOJ] 분해합
Link: https://www.acmicpc.net/problem/2231
Level: 브론즈 2
Tag : Python, brute force
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

num = int(input())

# 분해합 구하기
for i in range(1, num+1):
    if i + sum(map(int, list(str(i)))) == num:   # i를 문자열로 변환하여 합을 구하기
        print(i)
        break
    if i == num:
        print(0)
