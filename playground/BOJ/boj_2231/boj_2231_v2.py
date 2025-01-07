'''
----------------------------------------------
Sub : [BOJ] 분해합
Link: https://www.acmicpc.net/problem/2231
Tag : Python, 
Memo
----------------------------------------------
'''

num = int(input())
for i in range(1, num+1):
    if i + sum(map(int, list(str(i)))) == num:
        print(i)
        break
    if i == num:
        print(0)
