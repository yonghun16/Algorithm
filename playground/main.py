'''
----------------------------------------------
Sub: [BOJ] 1448. 삼각형 만들기(https://www.acmicpc.net/problem/1448)
Tag: py, greedy, sort
Memo:
----------------------------------------------
'''

import sys
input = sys.stdin.read
data = input().split()

print(data)

n = int(data[0])
inputDataList = list(map(int, data[1:n+1]))
