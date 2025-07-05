''' ----------------------------------------------
Sub : [BOJ] 소수 구하기
Link: https://www.acmicpc.net/problem/1929
Tag : Python, Math, Prime Number, Brute Force
Memo
---------------------------------------------- '''

import sys
input = sys.stdin.readline

# 입력 형식
m, n = map(int, input().strip().split())               # (1 ≤ M ≤ N ≤ 1,000,000)

# 결과 형식
answers = []

# 소수 찾기 : 시간복잡도 -> O(n*√m/2)                  # n=1,000,000, m=1,000,000 일 때 1,000,000*(√1,000,000)/2 = 1,000,000*(1,000)/2 = 5억
def is_prime_number(num):
    if num <= 1:                                       # num이 1보다 작은 수는 소수가 아님.
        return False
    elif num % 2 == 0 and num != 2:                    # num이 짝수이면 소수가 아님(2는 제외)
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):       # 3부터 num의 제곱근까지 홀수만 순서대로 나누기
            if num % i == 0:                           # 나누어 떨어지면 소수가 아님
                return False
    return True                                        # 살아남는 숫자는 소수임.

# 2는 따로 처리 (유일한 짝수 소수)
if m <= 2 <= n:
   answers.append(2)

# 홀수만 검사
start = max(3, m)
if start % 2 == 0:
    start += 1

# 소수 구하기
for num in range(start, n+1, 2):
    if is_prime_number(num):              # num이 소수이면
        answers.append(num)               # num을 answers에 추가

# 출력
for answer in answers:
    print(answer)
