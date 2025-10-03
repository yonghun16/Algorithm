# ------------------------------------------------------------
# Sub       : [BOJ] 나는야 포켓몬마스터 이다솜 (1620)
# Link      : https://www.acmicpc.net/problem/1620
# Level     : 실버 4
# Language  : Python
# Tags      : Dict, String
# Memo      : 번호 ↔ 이름 양방향 조회 구현
# ------------------------------------------------------------

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


# [문제 조건 파싱]
# m: 포켓몬 수, n: 문제 수
m, n = map(int, input().split())

# [데이터 구조]
# 번호 → 이름, 이름 → 번호 딕셔너리
pokemonDicNumber = {}
pokemonDicName = {}

# [사전 구성]
# 1번부터 m번까지 포켓몬 이름 입력
for i in range(1, m + 1):
    name = input().strip()
    pokemonDicNumber[i] = name  # 번호 → 이름
    pokemonDicName[name] = i  # 이름 → 번호

# [질의 처리 & 출력]
# m+1번째 줄부터 n개의 질의가 주어짐
for _ in range(n):
    query = input().strip()
    if query.isdigit():
        # query가 숫자면 번호로 조회
        print(pokemonDicNumber[int(query)])
    else:
        # query가 문자열이면 이름으로 조회
        print(pokemonDicName[query])
