"""
------------------------------------------------------------
Sub    : [BOJ] 수열의 합
Link   : https://www.acmicpc.net/problem/1024
Level  : 실버 2
Tag    : Python, math
Memo
------------------------------------------------------------
"""

import sys

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


N, L = map(int, input().split())

# 길이 L부터 100까지 시도
while L <= 100:
    startNum = N // L  # 초깃값을 N/L에서 시작
    while startNum >= 0:
        total = 0
        # startNum부터 L개를 직접 더한다
        for i in range(L):
            total += startNum + i

        if total == N:  # 찾았다!
            result = [startNum + i for i in range(L)]
            print(*result)
            exit(0)

        if total > N:  # 합이 더 크면 startNum을 줄여서 다시 시도
            startNum -= 1
        else:  # total < N -> 이 길이 L로는 부족하므로 종료 후 다음 L 시도
            break

    L += 1  # 길이를 늘리면서 다시 시도

# 못 찾았으면
print(-1)
