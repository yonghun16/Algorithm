''' ----------------------------------------------
Sub : [BOJ] 소수 구하기
Link: https://www.acmicpc.net/problem/1929
Tag : Python, Math, Prime Number, Brute Force
Memo
---------------------------------------------- '''

import sys
input = sys.stdin.readline

# 입력 형식
m, n = map(int, input().strip().split())  # (1 ≤ M ≤ N ≤ 1,000,000)

# 결과 형식
answers = []

# 소수 찾기 : 시간복잡도 -> O(n*m)        # n=1,000,000, m=1,000,000 일 때  n*m = 1조
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

# 소수 구하기
for num in range(m, n+1, 1):
    if is_prime_number(num):              # num이 소수이면
        answers.append(num)               # num을 answers에 추가

# 출력
for answer in answers:
    print(answer)
