'''----------------------------------------------------
Sub  : [BOJ] 오븐 시계
Link : https://www.acmicpc.net/problem/2525
Level: 브론즈 3
Tag  : Python, 사칙연산
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 형식
A, B = map(int, input().strip().split())  # 현재 시, 분
C = int(input().strip())                  # 요리 시간 (분)


# 출력 형식
class Answer:
    def __init__(self, hour, min):
        self.hour = hour                  # 요리 종료 시
        self.min = min                    # 요리 종료 분


# 입력 검사
def check_input(A, B, C):
    if A < 0 or A > 23 or B < 0 or B > 59 or C < 0 or C > 1000:
        raise ValueError("입력값이 허용 범위를 초과합니다.")

check_input(A, B, C);


# 알고리즘
def solution(A, B, C):
    # 분 단위로 변환 후 계산
    one_day_minute = 24 * 60;              # 하루 분
    total_minute = (A * 60) + B + C        # 요리 종료 시간
    total_minute %= one_day_minute         # 요리 종료 시각 : 하루가 넘어가는 경우는 하루 분(1440)으로 나누어 나머지 값으로 변경

    # 시, 분 계산
    hour = total_minute // 60
    min = total_minute % 60

    return hour, min


# 결과 출력
answer = Answer(*solution(A, B, C))
print(answer.hour, answer.min)
