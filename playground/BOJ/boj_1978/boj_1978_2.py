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

# 소수 찾기 : 시간복잡도 -> O(n*m/2)      # n=100, m=1,000 일 때 100*1,000/2 = 50,000
def is_prime_number(num):
    divided_count = 0                     # 나눈 횟수
    if num <= 1:                          # num이 1보다 작으면 소수가 아님
        return 0
    elif num == 2:                        # num이 2이면 소수
        return 1
    elif num % 2 == 0:                    # num이 짝수이면 소수가 아님
        return 0
    else:
        for i in range(1, num+1, 2):      # 1부터 num까지 홀수로 나누기
            if num % i == 0:              # 나누어 떨어지면
                divided_count += 1        # 나눈 횟수
                if divided_count > 2:     # 나눈 횟수가 2보다 크면 소수가 아님
                    return 0
    return 1                              # 살아남는 숫자는 소수임.

# 소수 갯수 구하기
for num in numbers:
    count += is_prime_number(num)         # 소수이면 1을 리턴하며, 그 return 값들을 count에 누적함.

# 출력
answer = count                            # 최종 count를 answer에 할당
print(answer)                             # answer 출력
