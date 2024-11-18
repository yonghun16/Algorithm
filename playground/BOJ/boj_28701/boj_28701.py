'''
----------------------------------------------
Sub : [BOJ] 
Link: https://www.acmicpc.net/problem/28701
Tag : Python, 
Memo
----------------------------------------------
'''

n = int(input())

sum = 0

for i in range(1, n+1):
    t = int(i)
    sum += t
print(sum)

print(sum*sum)

sum = 0
for i in range(1, n+1):
    t = int(i) * int(i) * int(i)
    sum += t
print(sum)
