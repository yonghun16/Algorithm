'''----------------------------------------------------
Sub  : [BOJ] 일곱 난쟁이
Link : https://www.acmicpc.net/problem/2309
Level: 브론즈 1
Tag  : Python, 브루투 포스
Memo
----------------------------------------------------'''

import sys
from itertools import combinations
input = sys.stdin.readline

# 입력 변수
height = [int(input().strip()) for _ in range(9)]

# 출력 변수
answer = []

# 7명의 조합 중 합이 100인 것을 찾기
for comb in combinations(height, 7):
    if sum(comb) == 100:
        answer = sorted(comb)
        break

# 출력
for i in answer:
    print(i)
