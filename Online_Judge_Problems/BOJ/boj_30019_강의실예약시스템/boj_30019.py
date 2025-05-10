'''---------------------------------------------
Sub  : [BOJ] 강의실 예약 시스템
Link : https://www.acmicpc.net/problem/30019
Level: 브론즈 2
Tag  : Python, 구현, 그리디
Memo
---------------------------------------------'''

import sys
input = sys.stdin.readline

def process_reservations(n, m, reservations):
    # 각 강의실에 대해 가장 최근의 끝 시각 저장
    latest_end_time = [0] * (n + 1)
    
    # 결과 저장 리스트
    result = []

    for k, s, e in reservations:
        # 현재 강의실의 가장 최근 끝 시각과 비교
        if latest_end_time[k] <= s:
            # 예약 가능
            result.append("YES")
            latest_end_time[k] = e
        else:
            # 예약 불가능
            result.append("NO")

    return result

# 입력 받기
import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
reservations = [tuple(map(int, line.split())) for line in data[1:]]

# 예약 처리 및 결과 출력
results = process_reservations(n, m, reservations)
print("\n".join(results))
