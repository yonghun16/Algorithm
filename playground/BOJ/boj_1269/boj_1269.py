'''----------------------------------------------------
Sub  : [BOJ] 대칭 차집합 
Link : https://www.acmicpc.net/problem/1269
Level: silver 4
Tag  : Python, 
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# input
n, m = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

# output
answer = 0

# process
C = A + B

for c in C:
    C.append(c)
    if C.count(c) >= 2:
        C.remove(c)
        C.remove(c)

print(len(C))
