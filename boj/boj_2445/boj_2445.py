'''-------------------------------------------
Sub : [BOJ] 별 찍기 - 8
Link: https://www.acmicpc.net/problem/2445
Tag : Python, 
Memo
-------------------------------------------'''

n = int(input())

for i in range(1, n + 1):
    print('*' * i, end="")
    print(' ' * int((n-i)*2), end="")
    print('*' * i, end="")
    print()
for i in range(1, n):
    print('*' * int(n-i), end="")
    print(' ' * int(i*2), end="")
    print('*' * int(n-i), end="")
    print()

