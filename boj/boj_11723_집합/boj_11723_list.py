# ------------------------------------------------------------
# Sub       : [BOJ] 집합
# Link      : https://www.acmicpc.net/problem/11723
# Level     : Silver 5 
# Tag       : Python, set
# Memo
# ------------------------------------------------------------

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


# input
M = int(input())
S = []

# checker 함수
def check(val):
    return val in S

# process
for _ in range(M):
    input_order = input().split()
    if len(input_order) > 1 :
        cmd = input_order[0]
        val = int(input_order[1])
    else :
        cmd = input_order[0]
        val = 0

    if cmd == "add":
        if not check(val): S.append(val)
    elif cmd == "remove":
        if check(val): S.remove(val)
    elif cmd == "check":
        print(1 if check(val) else 0)
    elif cmd == "toggle":
        if check(val): S.remove(val)
        else : S.append(val)
    elif cmd == "all":
        S = list(range(1, 21))
    elif cmd == "empty":
        S.clear()
