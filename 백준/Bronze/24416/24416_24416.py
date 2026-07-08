'''----------------------------------------------------
Sub  : [BOJ] 알고리즘 수업 - 피보나치 수 1
Link : https://www.acmicpc.net/problem/24416
Level: 브론즈 1
Tag  : Python, dynamic
Memo
 - count1[0]처럼 리스트를 쓴 이유는 포인터를 쓰기 위해서
----------------------------------------------------'''

import sys
input = sys.stdin.readline

def fib_recursive(n, count1):
    if n == 1 or n == 2:
        count1[0] += 1 
        return 1
    return fib_recursive(n - 1, count1) + fib_recursive(n - 2, count1)

def fibonacci_dp(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    count2 = 0
    
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count2 += 1
    
    return count2

# 입력
n = int(input().strip())

# 피보나치 수 재귀로 구하기
count1 = [0]
fib_recursive(n, count1)

# 피보나치 수 동적으로 구하기
count2 = fibonacci_dp(n)

# 출력
print(count1[0], count2)
