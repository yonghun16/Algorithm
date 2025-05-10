'''---------------------------------------------
Sub  : [BOJ] 2022년이 아름다웠던 이유
Link : https://www.acmicpc.net/problem/27065
Level: 브론즈 1
Tag  : Python, 수학, 구현
Memo
---------------------------------------------'''

import sys
input = sys.stdin.readline

# 약수
def find_divisors(number):
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != 1 and i != number // i:
                divisors.append(number // i)
    divisors.append(number)
    return divisors


# 과잉수 판별 함수
def is_abundant(n):
    divisors = find_divisors(n)
    sum_divisors = sum(divisors) - n  # 자기 자신 제외한 약수의 합

    return sum_divisors > n


# 부족수나 완전수 판별 함수
def are_all_divisors_deficient_or_perfect(n):
    divisors = find_divisors(n)
    divisors.remove(n)                # 자기 자신 제외
    for divisor in divisors:
        sum_div = sum(find_divisors(divisor)) - divisor
        if sum_div > divisor:         # 과잉수이면 False
            return False
    return True


# 메인 
T = int(input().strip())

for _ in range(T):
    n = int(input().strip())

    isOverNum = is_abundant(n)
    isLowComNum = are_all_divisors_deficient_or_perfect(n)

    if isOverNum and isLowComNum:
        print("Good Bye")
    else:
        print("BOJ 2022")
