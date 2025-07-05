'''
----------------------------------------------
Sub : [BOJ] 10!
Link: https://www.acmicpc.net/problem/28352
Tag : Python, 
Memo
----------------------------------------------
'''

n = int(input())
result = 1

while (n>0):
    result *= n
    n -= 1

result = int(result/60/60/24/7)
print(result)

