'''
----------------------------------------------
Sub : [BOJ] 
Link: https://www.acmicpc.net/problem/28701
Tag : Python, 
Memo
----------------------------------------------
'''

n = int(input())
sum_n = sum(range(1, n+1))
sum_n3 = sum(i**3 for i in range(1, n+1))

print(sum_n)
print(sum_n**2)
print(sum_n3)
