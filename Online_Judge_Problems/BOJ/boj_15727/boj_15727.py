'''
----------------------------------------------
Sub : [BOJ] 조별과제를 하려는데 조장이 사라졌다
Link: https://www.acmicpc.net/problem/15727
Tag : Python, 
Memo
----------------------------------------------
'''

import math

# 입력: 성우의 현재 위치와 민건이의 집까지의 거리 L
L = int(input().strip())

# 성우가 이동할 수 있는 최대 거리: 5
max_distance_per_minute = 5

# 최소 시간 계산
min_time = math.ceil(L / max_distance_per_minute)

# 결과 출력
print(min_time)
