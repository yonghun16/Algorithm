''' ----------------------------------------------
Sub : [BOJ] 최소, 최대
Link: https://www.acmicpc.net/problem/10818
Tag : Python, math
Memo
---------------------------------------------- '''

n = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums)) # 최소, 최대 출력
