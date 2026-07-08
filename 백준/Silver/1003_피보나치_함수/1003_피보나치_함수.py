"""------------------------------------------------------------
Sub       : [BOJ] 피보나치 함수
Link      : https://www.acmicpc.net/problem/1003
Level     : 실버 3
Tag       : Python, math
Memo
------------------------------------------------------------"""

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


t = int(input())
nums = [int(input()) for _ in range(t)]

# 최대 40까지 가능하므로 미리 DP 배열 계산
count_0 = [0] * 41
count_1 = [0] * 41

count_0[0], count_1[0] = 1, 0  # fibonacci(0)
count_0[1], count_1[1] = 0, 1  # fibonacci(1)

for i in range(2, 41):
    count_0[i] = count_0[i - 1] + count_0[i - 2]
    count_1[i] = count_1[i - 1] + count_1[i - 2]

# 각 테스트 케이스에 대한 결과 출력
for n in nums:
    print(count_0[n], count_1[n])
