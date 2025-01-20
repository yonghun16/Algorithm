'''---------------------------------------------
Sub  : [BOJ] 벌집
Link : https://www.acmicpc.net/problem/2292
Level: B2
Tag  : Python, 수학
Memo
 - 
---------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())

def find_min_rooms(N):
    if N == 1:
        return 1      # 중심은 방 하나로 충분
    
    layer = 1         # 껍질 수
    range_end = 1     # 각 껍질의 마지막 숫자

    while range_end < N:
        range_end += 6 * layer  # 다음 껍질 범위의 끝 계산
        layer += 1
    
    return layer


print(find_min_rooms(N))
