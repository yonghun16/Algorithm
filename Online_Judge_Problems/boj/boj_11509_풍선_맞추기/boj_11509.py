"""----------------------------------------------------
Sub  : [BOJ] 풍선 맞추기
Link : https://www.acmicpc.net/problem/11509
Level: 골드5
Tag  : Python, greedy
Memo
----------------------------------------------------"""

import sys

TEST_MODE = True


def get_inputs():
    if TEST_MODE:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip("\n")
    else:
        for line in sys.stdin:
            yield line.rstrip("\n")


input_gen = get_inputs()


def input():
    return next(input_gen)


# input
N = int(input().strip())
balloons = list(map(int, input().strip().split(" ")))
arrow_heights = [0] * 1000001
answer = 0

# processing
for ball in balloons:
    if arrow_heights[ball] > 0:
        arrow_heights[ball] -= 1
        arrow_heights[ball - 1] += 1
    else:
        arrow_heights[ball - 1] += 1
        answer += 1

# output
print(answer)
