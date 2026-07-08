'''
----------------------------------------------
Sub : [BOJ] 숫자의 합
Link: https://www.acmicpc.net/problem/11720
Tag : Python
Memo
----------------------------------------------
'''

N = int(input())

s = input()

sum = 0

for i in range(N):
    sum += int(s[i])

print(sum)
