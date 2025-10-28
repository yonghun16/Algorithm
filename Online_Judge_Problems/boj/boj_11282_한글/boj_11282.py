# ------------------------------------------------------------
# Sub       : [BOJ] 한글
# Link      : https://www.acmicpc.net/problem/11282
# Level     : 브론즈 4
# Tag       : Python,
# Memo
# ------------------------------------------------------------

import sys

# [환경 설정]
TEST_MODE = False


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


N = int(input())
print(chr(0xAC00 + (N - 1)))
