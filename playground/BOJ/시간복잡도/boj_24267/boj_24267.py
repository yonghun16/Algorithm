'''----------------------------------------------------
Sub  : [BOJ] 알고리즘의 수행시간 6
Link : https://www.acmicpc.net/problem/24267
Level: 브론즈 2
Tag  : Python, BigO
Memo
----------------------------------------------------'''

import sys
import random
input = sys.stdin.readline

n = int(input())
# A = [random.randint(1, 10) for _ in range(n+1)]

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

# def MenOfPassion(A, n):
#     count = 0
#     sum = 0
#     for i in range(1, n-1):
#         for j in range(i+1, n):
#             for k in range(j+1, n+1):
#                 sum += A[i] * A[j] * A[k]
#                 count += 1
#     # return sum
#     return count
#
# result_count = MenOfPassion(A, n)

# 결과 출력
# 시간복잡도 -> O(n^3)
# print(result_count)
print(n * (n-1) * (n-2) // 6)
print(3)

