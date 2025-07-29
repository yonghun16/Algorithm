'''----------------------------------------------------
Sub  : [BOJ] 회의실 배정
Link : https://www.acmicpc.net/problem/1939
Level: 골드 5
Tag  : Python, greddy
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
n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 정렬 기준을 함수로 정의
def sort_key(meeting):
    return (meeting[1], meeting[0])  # (끝나는 시간, 시작 시간)

# 정렬 수행
meetings.sort(key=sort_key)

end_time = 0
answer = 0

for start, end in meetings:
    if start >= end_time:
        end_time = end
        answer += 1

print(answer)
