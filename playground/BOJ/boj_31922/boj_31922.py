''' 이 대회는 이제 제 겁니다
----------------------------------------------
Sub : [BOJ] 
Link: https://www.acmicpc.net/problem/31922
Tag : Python, 
Memo
----------------------------------------------
'''

A, P, C = map(int, input().split())

max_prize = max(A + C, P)

print(max_prize)
