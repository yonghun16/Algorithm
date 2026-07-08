'''----------------------------------------------------
Sub  : [BOJ] 큐
Link : https://www.acmicpc.net/problem/10845
Level: 실버 4
Tag  : Python, Queue
Memo
----------------------------------------------------'''

import sys
from collections import deque

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
N = int(input().strip())
q = deque()

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(1 if not q else 0)
    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
