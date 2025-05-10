'''---------------------------------------------
Sub  : [BOJ] 피씨방 알바
Link : https://www.acmicpc.net/problem/1453
Level: 브론즈 2
Tag  : Python, 구현
Memo
 - 
---------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
seats = list(map(int, input().split()))

def count_rejected_customers(seats):
    occupied = set()
    rejected = 0

    for seat in seats:
        if seat in occupied:
            rejected += 1
        else:
            occupied.add(seat)

    print(rejected)

# 함수 실행
count_rejected_customers(seats)
