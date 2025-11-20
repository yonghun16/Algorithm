"""
------------------------------------------------------------
Sub    : [BOJ] 최소 힙
Link   : https://www.acmicpc.net/problem/1927
Level  : 실버 2
Tag    : Python, heap
Memo
------------------------------------------------------------
"""

import sys
import heapq

# [환경 설정]
TEST_MODE = True


# [입력 처리 함수]
def get_inputs():
    # 로컬 테스트 (input.txt 파일 읽기)
    if TEST_MODE:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip("\n")
    else:
        # 제출 환경 (표준 입력)
        for line in sys.stdin:
            yield line.rstrip("\n")


input_gen = get_inputs()


def input():
    return next(input_gen)


n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap))  # 최소값 제거 후 출력
        else:
            print(0)
    else:
        heapq.heappush(heap, x)  # 힙에 값 추가
