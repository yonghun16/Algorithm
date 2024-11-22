'''
----------------------------------------------
Sub : [BOJ] 웰컴 키트
Link: https://www.acmicpc.net/problem/30802
Tag : Python, 
Memo
----------------------------------------------
'''

n = int(input())
student = list(map(int, input().split()))
t, p = map(int, input().split())

t_count = 0

for i in student:
    t_count += int(i/t)
    if(i%t > 0):
        t_count += 1

print(t_count)
print(int(n/p), n%p)
