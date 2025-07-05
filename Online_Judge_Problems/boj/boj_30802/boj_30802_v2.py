'''
----------------------------------------------
Sub : [BOJ] 웰컴 키트
Link: https://www.acmicpc.net/problem/30802
Tag : Python, 
Memo
----------------------------------------------
'''

import math

N = int(input())  # 참가자의 수
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())  # 티셔츠와 펜의 묶음 크기

# 티셔츠 최소 묶음 계산
# 각 사이즈별 필요한 티셔츠 수를 T로 나눠 묶음 수를 계산하고 올림한다.
sizes = [S, M, L, XL, XXL, XXXL]
min_tshirt_bundles = sum(math.ceil(size / T) for size in sizes)

# 펜 최대 묶음 및 남은 펜 개수 계산
# 참가자 수 N을 P로 나눠 묶음 수를 계산하고, 나머지로 남은 펜 개수를 구한다.
max_pen_bundles = N // P
remaining_pens = N % P

# 결과 출력
print(min_tshirt_bundles)
print(max_pen_bundles, remaining_pens)
