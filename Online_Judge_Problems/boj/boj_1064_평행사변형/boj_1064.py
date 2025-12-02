"""
------------------------------------------------------------
Sub    : [BOJ] 평행사변형
Link   : https://www.acmicpc.net/problem/1064
Level  : 실버 4
Tag    : Python,
Memo
------------------------------------------------------------
"""

import sys
import math

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


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def solve():
    xA, yA, xB, yB, xC, yC = map(float, input().split())
    A = (xA, yA)
    B = (xB, yB)
    C = (xC, yC)

    # 세 점이 일직선인지 체크 (면적 = 0)
    area = xA * (yB - yC) + xB * (yC - yA) + xC * (yA - yB)
    if abs(area) < 1e-12:
        print(-1.0)
        return

    perimeters = []

    def add_case(P, Q, R):
        """
        평행사변형 P Q R 에서 P를 기준으로 Q,R이 인접 변,
        D1 = Q + (R - P)
        D2 = R + (Q - P)
        둘 다 평행사변형이므로 둘레 동일.
        """
        v1 = (Q[0] - P[0], Q[1] - P[1])
        v2 = (R[0] - P[0], R[1] - P[1])
        L1 = math.hypot(v1[0], v1[1])
        L2 = math.hypot(v2[0], v2[1])
        perimeters.append(2 * (L1 + L2))

    # 3가지 가능한 평행사변형 배치
    add_case(A, B, C)
    add_case(B, A, C)
    add_case(C, A, B)

    if not perimeters:
        print(-1.0)
    else:
        print(max(perimeters) - min(perimeters))


if __name__ == "__main__":
    solve()
