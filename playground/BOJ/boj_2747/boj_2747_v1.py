'''---------------------------------------------
Sub  : [BOJ] 피보나치 수
Link : https://www.acmicpc.net/problem/2747
Level: Bronze 2
Tag  : Python, 수학, 구현, 다이나믹
Memo
 - a, b = b, a+b에서 b = a+b -> 이전에 구했던 a의 값을 사용
---------------------------------------------'''

import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a+b
    return b

# 입력 받기
n = int(input().strip())

# n번째 피보나치 수 출력
print(fibonacci(n))
