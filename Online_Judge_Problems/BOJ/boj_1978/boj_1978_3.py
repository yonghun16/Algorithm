''' ----------------------------------------------
Sub : [BOJ] 소수 찾기
Link: https://www.acmicpc.net/problem/1978
Tag : Python, Math, Prime Number, Brute Force
Memo
---------------------------------------------- '''

import sys
input = sys.stdin.readline

# 입력 형식
n = int(input().strip())                              # n -> 입력 개수(100개이하)
numbers = [int(_) for _ in input().strip().split()]   # 자연수(1000이하)

# 출력 형식
answer = count = 0                        # 소수의 갯수

# 소수 찾기 : 시간복잡도 -> O(n*√m/2)     # n=100, m=1000 일 때 100*(√1,000)/2 = 100*(31.62)/2 = 약1,581
def is_prime_number(num):
    if num <= 1:                          # num이 1보다 작은 수는 소수가 아님.
        return False
    elif num % 2 == 0 and num != 2:       # num이 짝수이면 소수가 아님(2는 제외)
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2): # 3부터 num의 제곱근까지 홀수만 순서대로 나누기
            if num % i == 0:              # 나누어 떨어지면 소수가 아님
                return False
    return True                           # 살아남는 숫자는 소수임.

# 소수 갯수 구하기
for num in numbers:
    if is_prime_number(num):              # num이 소수이면
        count += 1                        # count에 1씩 더함.

# 출력
answer = count                            # 최종 count를 answer에 할당
print(answer)                             # answer 출력
