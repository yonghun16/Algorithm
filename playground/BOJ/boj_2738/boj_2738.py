'''
----------------------------------------------
Sub: [BOJ] 2738. 행렬 덧셈
Link: https://www.acmicpc.net/problem/2738
Tag: python, 2차원 배열
Memo
----------------------------------------------
'''

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    result = []
    for j in range(M):
        result.append(A[i][j] + B[i][j])
    print(' '.join(map(str, result)))
