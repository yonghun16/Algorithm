'''---------------------------------------------
Sub  : [BOJ] 피보나치 수
Link : https://www.acmicpc.net/problem/2747
Level: Bronze 2
Tag  : Python, 수학, 구현, 다이나믹
Memo
 - 재귀를 사용
 - 백준에서는 시간초과가 발생함.
---------------------------------------------'''

import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 입력 받기
n = int(input().strip())

# n번째 피보나치 수 출력
print(fibonacci(n))
