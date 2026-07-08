'''----------------------------------------------------
Sub  : [BOJ] 요세푸스 문제0
Link : https://www.acmicpc.net/problem/11866
Level: 실버 4
Tag  : Python, Deque
Memo
----------------------------------------------------'''

from collections import deque
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


# 입력
N, K = map(int, input().strip().split())

# 풀이
def josephus(N, K):
    q = deque(range(1, N+1))
    result = []
    while q:
        q.rotate(-(K-1))       # K번째 사람이 앞으로 오도록 회전
        result.append(q.popleft())
    return result

# 출력
result = josephus(N, K)
print("<" + ", ".join(map(str, result)) + ">")
