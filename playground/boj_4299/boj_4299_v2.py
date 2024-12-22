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


if x<0 or y<0 or x - int(x) > 0.0  or  y - int(y) > 0.0:
    print(-1)
else:
    if y > x:
        print(int(y), int(x))
    else:
        print(int(x), int(y))
