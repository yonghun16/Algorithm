'''
----------------------------------------------
Sub : [BOJ] 직각삼각형
Link: https://www.acmicpc.net/problem/4153
Tag : Python, math
Memo
----------------------------------------------
'''

import sys
input = sys.stdin.read

def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2

data = input().strip().split('\n')

for line in data:
    a, b, c = map(int, line.split())
    if a == 0 and b == 0 and c == 0:
        break
    if is_right_triangle(a, b, c):
        print("right")
    else:
        print("wrong")
