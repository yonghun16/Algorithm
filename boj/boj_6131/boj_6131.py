'''----------------------------------------------------
Sub  : [BOJ] 완전 제곱수
Link : https://www.acmicpc.net/problem/6131
Level: 브론즈 3
Tag  : python, Brute Force
Memo
  - b를 기준으로 a를 비교하고
  - a와 b 중에서 어떤 값이 높아지면 더이상 반복할 필요가 없는지?
----------------------------------------------------'''

import sys
input = sys.stdin.readline

MAX = 500
a = 1
b = 1
count = 0

# 입력
n = int(input().strip())

while b < MAX:
    if a**2 == b**2 + n:
        count += 1
        b += 1
        a = b
    elif a**2 > b**2 + n:
        b += 1
        a = b
        continue
    a += 1

# 출력
print(count)
