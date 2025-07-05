'''----------------------------------------------------
Sub  : [BOJ] 평균
Link : https://www.acmicpc.net/problem/1546
Level: 브론즈 1
Tag  : Python,
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력
n = int(input().rstrip())
scores = list(map(int, input().rstrip().split()))

#최대값
max_score = max(scores)

average_score = sum((score / max_score) * 100 for score in scores) / n

# 출력
print(average_score)
