'''----------------------------------------------------
Sub  : [BOJ] 좌표 정렬하기
Link : https://www.acmicpc.net/problem/11650
Level: 실버 5
Tag  : Python, 정렬
Memo
----------------------------------------------------'''

import sys

TEST_MODE = True  # True -> file input, False -> stdin input

def get_inputs():
    if TEST_MODE:
        with open('input2.txt', 'r') as f:
            for line in f:
                yield line.rstrip('\n')
    else:
        for line in sys.stdin:
            yield line.rstrip('\n')

input_gen = get_inputs()

def input():
    return next(input_gen)


# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(1, N + 1)]


# 정렬
arr.sort(key=lambda x: (x[0], x[1]))


# 출력
for x, y in arr:
    print(x, y)
