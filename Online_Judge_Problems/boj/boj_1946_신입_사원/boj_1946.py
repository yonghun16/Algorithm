'''----------------------------------------------------
Sub  : [BOJ] 신입 사원
Link : https://www.acmicpc.net/problem/1946
Level: 실버 1
Tag  : Python, greedy
Memo
----------------------------------------------------'''

import sys

TEST_MODE = True

def get_inputs():
    if TEST_MODE:
        with open('input.txt', 'r') as f:
            for line in f:
                yield line.rstrip('\n')
    else:
        for line in sys.stdin:
            yield line.rstrip('\n')

input_gen = get_inputs()

def input():
    return next(input_gen)


# solution
def sol(score):
    score.sort(key=lambda x: x[0])    # 서류 기준 오름차순

    min_interview = score[0][1]
    count = 1

    for i in range(1, len(score)):
        if score[i][1] < min_interview:
            count += 1
            min_interview = score[i][1]

    return count


# input
T = int(input())

for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]

    # output
    print(sol(score))
