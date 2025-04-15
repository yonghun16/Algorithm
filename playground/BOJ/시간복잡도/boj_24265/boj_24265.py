'''----------------------------------------------------
Sub  : [BOJ] 알고리즘의 수행 시간4
Link : https://www.acmicpc.net/problem/24265
Level: 브론즈 3
Tag  : Python, BigO
Memo
----------------------------------------------------'''

import sys
import random
input = sys.stdin.readline

n = int(input().strip())
# A = [random.randint(1, 10) for _ in range(n+1)]

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''


# def MenOfPassion(A, n):
#     count = 0
#     sum = 0
#     for i in range(1, n):
#         for j in range(i + 1, n+1):
#             sum += A[i] * A[j]
#             count += 1
#     return count
#
# result_count = MenOfPassion(A, n)

# 결과출력
# 시간복잡도 -> O(n^2)
# print(result_count)
print(n * (n - 1) // 2)    # n(n-1)/2 횟수 반복
print(2)                   # O(n^2)의 차수는 2

