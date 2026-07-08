"""
------------------------------------------------------------
Sub    : [BOJ] 암기왕
Link   : https://www.acmicpc.net/problem/2776
Level  : 실버 4
Tag    : Python, 이진 탐색
Memo
------------------------------------------------------------
"""

import sys

sys.setrecursionlimit(10**7)

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


def binary_search(arr, target, left, right):
    if left > right:  # 더 이상 탐색할 구간이 없다면
        return 0
    mid = (left + right) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


T = int(input())

for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()

    M = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        print(binary_search(note1, num, 0, N - 1))
