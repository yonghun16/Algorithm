'''----------------------------------------------------
Sub  : [BOJ] A->B
Link : https://www.acmicpc.net/problem/16953
Level: 실버 2
Tag  : Py, greedy
Memo
----------------------------------------------------'''

import sys

TEST_MODE = True

def get_inputs():
    if TEST_MODE:
        with open('input1.txt', 'r') as f:
            for line in f:
                yield line.rstrip('\n')
    else:
        for line in sys.stdin:
            yield line.rstrip('\n')

input_gen = get_inputs()

def input():
    return next(input_gen)


# input
A, B = map(int, input().split())


# solution
answer = 0
while B > A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break
    answer += 1


# check if transformation is successful
if B == A:
    print(answer + 1)
else:
    print(-1)
