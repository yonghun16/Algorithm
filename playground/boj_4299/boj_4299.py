'''
----------------------------------------------
Sub : [BOJ] AFC
Link: https://www.acmicpc.net/problem/4299
Tag : Python, math
Memo
----------------------------------------------
'''

import numpy as np

a, b = map(int, input().split())

A = np.array([
    [1, 1],
    [1, -1]
])

B = np.array([a, b])

X = np.linalg.solve(A, B)

if (X[0] - int(X[0]) or X[1] - int(X[1])) > 0.0:
    print(-1)
else:
    print(int(X[0]), int(X[1]))

