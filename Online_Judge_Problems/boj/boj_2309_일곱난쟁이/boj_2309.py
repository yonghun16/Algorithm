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

# 7명의 조합 중 합이 100인 것을 찾기
total_height = 100
for i1 in range(3):
    for i2 in range(i1+1, 4):
        for i3 in range(i2+1, 5):
            for i4 in range(i3+1, 6):
                for i5 in range(i4+1, 7):
                    for i6 in range(i5+1, 8):
                        for i7 in range(i6+1, 9):
                            sum_height = (
                                height[i1] + height[i2] + 
                                height[i3] + height[i4] + 
                                height[i5] + height[i6] + height[i7])
                            if sum_height == total_height:
                                answer = sorted([
                                    height[i1], height[i2], 
                                    height[i3], height[i4], 
                                    height[i5], height[i6], height[i7]])

# 출력
for i in answer:
    print(i)
