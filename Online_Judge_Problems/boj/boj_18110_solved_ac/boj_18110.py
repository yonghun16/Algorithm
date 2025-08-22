'''----------------------------------------------------
Sub  : [BOJ] Solved.ac
Link : https://www.acmicpc.net/problem/18110
Level: 실버 4
Tag  : Python, math
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
if n == 0:
    print(0)
    exit()

opinions = [int(input().strip()) for _ in range(n)]
opinions.sort()

# 0.15*n 을 반올림(half-up) -> (3n/20) half-up == (3n + 10)//20
cut = (3 * n + 10) // 20

# 절사 구간 합과 개수
lo, hi = cut, n - cut
total = sum(opinions[lo:hi])
m = hi - lo  # 남은 개수

# print
# 평균을 반올림(half-up): floor(S/m + 0.5) = (2S + m)//(2m)
answer = (total * 2 + m) // (2 * m)
print(answer)
