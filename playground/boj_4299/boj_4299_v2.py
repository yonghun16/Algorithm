'''
----------------------------------------------
Sub : [BOJ] AFC
Link: https://www.acmicpc.net/problem/4299
Tag : Python, math
Memo
----------------------------------------------
'''

a, b = map(int, input().split())

y = (a+b)/2

x = a-y


if x - int(x) > 0.0 or y - int(y) > 0.0:
    print(-1)
else:
    print(int(y), int(x))
