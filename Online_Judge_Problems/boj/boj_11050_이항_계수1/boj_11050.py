'''----------------------------------------------------
Sub  : [BOJ] 이항 계수 1
Link : https://www.acmicpc.net/problem/11050
Level: 브론즈 1
Tag  : Python, math
Memo
----------------------------------------------------'''

import math

# 입력 받기
N, K = map(int, input().split())

# 이항계수 계산
result = math.comb(N, K)

# 출력
print(result)
