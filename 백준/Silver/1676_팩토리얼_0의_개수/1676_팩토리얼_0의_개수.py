'''----------------------------------------------------
Sub  : [BOJ] 
Link : https://www.acmicpc.net/problem/1676
Level: 실버 5
Tag  : Python, math
Memo
 - 숫자 10이 하나의 0을 만드니, 10 = 2 × 5 라고 보면 된다. 
 - 팩토리얼에서는 보통 2의 개수보다 5의 개수가 적기 때문에, 
 - 5의 개수를 세면 trailing zero 개수를 알 수 있다.
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

# processing
count = 0
p = 5

while p <= N:
    count += N // p
    p *= 5

# print
print(count)
