'''
----------------------------------------------
Sub : [BOJ] 별찍기-2
Link: https://www.acmicpc.net/problem/2439
Tag : Python
Memo
----------------------------------------------
'''

N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i), end='')
    print('*' * i)
