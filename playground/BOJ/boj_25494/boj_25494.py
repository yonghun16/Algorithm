'''
----------------------------------------------
Sub : [BOJ] 단순한 문제 (Small)
Link: https://www.acmicpc.net/problem/25494
Tag : Python, Brute Force, math
Memo
----------------------------------------------
'''

n = int(input())

def match(a, b, c):
    count = 0
    for x in range(1, a+1):
        for y in range(1, b+1):
            for z in range(1, c+1):
                if x%y == y%z == z%x:
                    count += 1
    return count


for i in range(n):
    a, b, c = map(int, input().split())
    print(match(a, b, c))
