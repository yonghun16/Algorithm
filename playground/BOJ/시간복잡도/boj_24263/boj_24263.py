'''----------------------------------------------------
Sub  : [BOJ] 알고리즘의 수행시간 2
Link : https://www.acmicpc.net/problem/
Level: 브론즈 4
Tag  : Python, BigO
Memo
----------------------------------------------------'''

import sys
import random
input = sys.stdin.readline

n = int(input().strip())
A = [random.randint(1, 10) for _ in range(n+1)]

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}
'''

def MenOfPassion(A, n):
    count = 0
    sum = 0
    for i in range(1, n+1):
        sum += A[i]
        count += 1
    # return sum
    return count

result_count = MenOfPassion(A, n)


# 결과 출력
# 시간복잡도 -> O(n)
# print(result_count)  # O(n)
print(n)             # O(1)
print(1)             # O(n)의 차수 -> 1
