'''
----------------------------------------------
Sub : [BOJ] 웰컴 키트
Link: https://www.acmicpc.net/problem/30802
Tag : Python, 
Memo
----------------------------------------------
'''

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

min_tshirt_bundles = 0

for i in size:
    min_tshirt_bundles += int(i/t)
    if(i%t > 0):
        min_tshirt_bundles += 1

print(min_tshirt_bundles)
print(int(n/p), n%p)
