'''----------------------------------------------------
Sub  : [BOJ] 지영 공주님의 마법 거울
Level: 브론즈 3
Tag  : Python, String
Memo
 - python의 2차원 배열 출력 방법 잘 익히기
 - 슬라이싱 인덱싱 잘 다루기
----------------------------------------------------'''

import sys
input = sys.stdin.readline

N = int(input().strip())
mirror = []

for _ in range(N):
    row = list(map(str, input().strip()))
    mirror.append(row)

K = int(input().strip())

# K 값에 따른 변환
if K == 1:
    for row in mirror:
        for element in row:
            print(element, end='')
        print()

elif K == 2:
    for row in mirror:
        for element in reversed(row):
            print(element, end='')
        print()

elif K == 3 :
    for row in reversed(mirror):
        for element in row:
            print(element, end='')
        print()
