'''----------------------------------------------------
Sub  : [BOJ] 수 찾기
Link : https://www.acmicpc.net/problem/1920
Level: 실버 4
Tag  : Python, 이진 탐색
Memo : 
----------------------------------------------------'''

import sys

TEST_MODE = False

def inputs():
    if TEST_MODE:
        with open('input.txt', 'r') as f:
            return f.read().split()
    else:
        return sys.stdin.read().split()


import bisect

# input
data = list(map(int, inputs()))

idx = 0
N = data[idx]; idx += 1
A = sorted(data[idx:idx+N]); idx += N

M = data[idx]; idx += 1
B = data[idx:idx+M]

for num in B:
    pos = bisect.bisect_left(A, num)  # bisect_left(A, num) → num이 삽입될 수 있는 왼쪽 인덱스를 반환
    if pos < N and A[pos] == num:
        print(1)
    else:
        print(0)
