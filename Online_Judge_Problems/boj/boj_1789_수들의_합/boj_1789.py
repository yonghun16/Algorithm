'''----------------------------------------------------
Sub  : [BOJ] 수들의 합
Link : https://www.acmicpc.net/problem/1789
Level: 실버 5
Tag  : Python, greedy
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
S = int(input())


# solution
acc = 0
count = 0

for i in range(1, S+1):
    acc += i
    count += 1
    if acc > S:
        count -= 1
        break


# output
print(count)
