'''----------------------------------------------------
Sub  : [BOJ] 일곱 난쟁이
Link : https://www.acmicpc.net/problem/2309
Level: 브론즈 1
Tag  : Python, 브루투 포스
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 변수
height = [int(input().strip()) for _ in range(9)]

# 출력 변수
answer = []

# 2명을 골라서 전체합 - 두명의 합 == 100인지 확인
total = sum(height)
found = False
for i in range(8):
    for j in range(i + 1, 9):
        if total - (height[i] + height[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    answer.append(height[k])
            found = True
            break
    if found:
        answer = sorted(answer)
        break

# 출력
for i in answer:
    print(i)
