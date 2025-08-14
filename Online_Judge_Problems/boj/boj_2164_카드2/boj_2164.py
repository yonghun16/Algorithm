'''----------------------------------------------------
Sub  : [BOJ]  카드2
Link : https://www.acmicpc.net/problem/2164
Level: 실버 4
Tag  : Python, queue
Memo
----------------------------------------------------'''

import sys

TEST_MODE = False

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
card = list(range(1, N + 1))

# processing
current_list = card

while len(current_list) > 1:
    current_list = current_list[1::2]              # 1. 버리기 (짝수 위치 카드만 남김)
    if len(current_list) > 1 and N % 2 == 1:
        current_list.append(current_list.pop(0))   # 2. 실제 규칙에 맞게 회전 보정
    N = len(current_list)                          # 3. 다음단계 준비 

print(current_list[0])
