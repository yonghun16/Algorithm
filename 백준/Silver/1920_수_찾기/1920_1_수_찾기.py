import sys
input = sys.stdin.read
data = list(map(int, input().split()))

idx = 0
N = data[idx]; idx += 1
A = data[idx:idx+N]; idx += N

M = data[idx]; idx += 1
B = data[idx:idx+M]

A_set = set(A)

for num in B:
    print(1 if num in A_set else 0)
