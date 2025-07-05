''' ----------------------------------------------
Sub : [BOJ] 소수 구하기
Link: https://www.acmicpc.net/problem/1929
Tag : Python, Math, Prime Number, Brute Force
Memo
---------------------------------------------- '''

import sys
input = sys.stdin.readline

# 입력 형식
m, n = map(int, input().strip().split())                  # (1 ≤ M ≤ N ≤ 1,000,000)

# 결과 형식
answers = []

# 에라토스테네스의 체로 소수 찾기
# 시간복잡도 -> O(m log log m)                            # m=1,000,000 일 때, 1,000,000 * log(log1,000,000) = 약778,200
def eratostheneses_sieve(m, n):
    max_num = n
    is_prime = [False, False] + [True] * (max_num - 1)    # numbers의 2부터 최대값까지 1로 초기화하여 소수일 가능성이 있다고 가정.

    for i in range(2, int(max_num ** 0.5) + 1):           # 2부터 num의 제곱근까지
        if is_prime[i]:                                   # 소수라고 가정한 숫자이면
            for j in range(i * i, max_num + 1, i):        # 각 수의 배수를 모두 제거
                is_prime[j] = False

    for num in range(m, n+1):
        if is_prime[num]:                                 # num이 소수이면
            answers.append(num)                           # num을 answers에 추가

# 함수 호출
eratostheneses_sieve(m, n)

# 출력
for answer in answers:
    print(answer)
