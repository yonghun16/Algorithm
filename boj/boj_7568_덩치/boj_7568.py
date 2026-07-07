'''----------------------------------------------------
Sub  : [BOJ] 덩치
Link : https://www.acmicpc.net/problem/7568
Level: 실버 5
Tag  : Python, brute force
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

# input
n = int(input().strip())
people = [tuple(map(int, input().split())) for _ in range(n)]


#processing
ranks = []
for i in range(n):
    count = 0
    for j in range(n):
        if i != j:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                count += 1
    ranks.append(count + 1)


#output
print(*ranks)
