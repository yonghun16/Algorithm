'''----------------------------------------------------
Sub  : [BOJ] 달팽이는 올라가고 싶다
Link : https://www.acmicpc.net/problem/2869
Level: 브론즈 1
Tag  : Python, 수학
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 받기
A, B, V = map(int, input().strip().split())

days_count = int((V-A) / (A-B))
distance = days_count * (A-B)
answer = 0

while True:
    days_count += 1
    distance += A
    if distance >= V:
        answer = days_count
        break
    else:
        distance -= B

# 출력하기
print(answer)
