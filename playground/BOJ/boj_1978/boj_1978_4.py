''' ----------------------------------------------
Sub : [BOJ] 소수 찾기
Link: https://www.acmicpc.net/problem/1978
Tag : Python, Math, Prime Number, Brute Force
Memo
  - 에라토스테네스의 체
	1.	1을 제외한 모든 수를 소수일 가능성이 있다고 가정합니다.
	2.	2부터 시작하여 각 수의 배수를 모두 제거합니다. 2는 소수이므로, 2의 배수는 소수가 아니라고 표시합니다.
	3.	그 다음으로 남아있는 수 중에서 가장 작은 수인 3을 선택하고, 3의 배수를 모두 제거합니다.
	4.	이 과정을 제곱근까지 반복하면서 남은 수는 소수로 간주합니다.
---------------------------------------------- '''

import sys
input = sys.stdin.readline

# 입력 형식
n = int(input().strip())                              # n -> 입력 개수(100개이하)
numbers = [int(_) for _ in input().strip().split()]   # 자연수(1000이하)

# 출력 형식
answer = count = 0                                    # 소수의 갯수

# 에라토스테네스의 체
# 시간복잡도 -> O(m log log m)                        # m=1000 일 때, 1000 * log(log1000) = 약477.1
max_num = max(numbers)                                # numbers의 최대값
is_prime = [0, 0] + [1] * (max_num - 1)               # numbers의 2부터 최대값까지 1로 초기화하여 소수일 가능성이 있다고 가정.
for i in range(2, int(max_num ** 0.5) + 1):           # 2부터 num의 제곱근까지
    if is_prime[i]:                                   # 소수라고 가정한 숫자이면
        for j in range(i * i, max_num + 1, i):        # 각 수의 배수를 모두 제거
            is_prime[j] = 0

# 주어진 수 중에서 소수만 세기
for num in numbers:
    count += is_prime[num]

#출력
answer = count
print(answer)
