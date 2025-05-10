'''----------------------------------------------------
Sub  : [BOJ] 지영 공주님의 마법 거울
Level: 브론즈 3
Tag  : Python, String
Memo
 - 리스트 안에 for를 사용해서 입력받기
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
mirror = [input().strip() for _ in range(N)]
K = int(input().strip())

# K 값에 따른 변환
result = []
if K == 1:
    result = mirror  # 그대로 출력
elif K == 2:
    result = [row[::-1] for row in mirror]  # 좌우 반전
elif K == 3:
    result = mirror[::-1]  # 상하 반전

# 결과 출력
print("\n".join(result))
