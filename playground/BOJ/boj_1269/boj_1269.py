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
C = []

for a in A:
    C.append(a)
    if C.count(a) >= 2:
        C.remove(a)
        C.remove(a)

for b in B:
    C.append(b)
    if C.count(b) >= 2:
        C.remove(b)
        C.remove(b)

print(len(C))
