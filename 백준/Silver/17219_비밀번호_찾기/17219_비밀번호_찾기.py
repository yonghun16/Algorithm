"""------------------------------------------------------------
Sub       : [BOJ] 비밀번호 찾기
Link      : https://www.acmicpc.net/problem/17219
Level     : 실버 4
Tag       : Python, map
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


# N: 저장된 사이트 수, M: 찾으려는 사이트 수
N, M = map(int, input().split())

# 비밀번호를 저장할 딕셔너리
passwords = {}

# N개의 사이트 주소와 비밀번호 입력
for _ in range(N):
    site, pw = input().split()
    passwords[site] = pw

# M개의 사이트 주소를 입력받고, 해당 비밀번호 출력
for _ in range(M):
    site = input().strip()
    print(passwords[site])
