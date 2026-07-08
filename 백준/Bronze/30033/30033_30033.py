'''
----------------------------------------------
Sub : [BOJ] Rust Study
Link: https://www.acmicpc.net/problem/30033
Tag : Python
Memo
----------------------------------------------
'''

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0

for i in range(N):
    if B[i] >= A[i]:
        count += 1

print(count)
