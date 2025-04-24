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

# 소수 찾기 : 시간복잡도 -> O(n*m)        # n=100, m=1,000 일 때 100*1,000 = 100,000
def is_prime_number(num):
    divided_count = 0                     # 나눈 횟수
    if num <= 1:                          # num이 1보다 작으면 소수가 아님
        return False                      # False 반환(소수가 아님)
    elif num == 2:                        # num이 2이면 소수
        return True                       # True를 반환(소수)
    else:
        for i in range(1, num+1):         # 1부터 num까지 순서대로 나누기
            if num % i == 0:              # 나누어 떨어지면
                divided_count += 1        # 나눈 횟수
                if divided_count > 2:     # 나눈 횟수가 2보다 크면, 즉 소수가 아니면
                    return False          # False를 반환(소수가 아님)
    return True                           # True를 반환(소수)

# 소수 갯수 구하기
for num in numbers:
    if is_prime_number(num):              # num이 소수이면
        count += 1                        # count에 1씩 더함.

# 출력
answer = count                            # 최종 count를 answer에 할당
print(answer)                             # answer 출력
