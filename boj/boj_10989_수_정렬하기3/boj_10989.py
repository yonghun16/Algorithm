'''----------------------------------------------------
Sub  : [BOJ] 수 정렬하기 3
Link : https://www.acmicpc.net/problem/10989
Level: 브론즈 1
Tag  : Python, sort
Memo
----------------------------------------------------'''

import sys

# 입력 최적화
input = sys.stdin.readline

# 수의 개수 N 입력
N = int(input())

# 숫자 범위가 1부터 10,000까지이므로 크기 10001짜리 리스트 생성
counts = [0] * 10001

# 숫자 개수 세기
for _ in range(N):
    num = int(input())
    counts[num] += 1

# 오름차순으로 출력
for num in range(1, 10001):
    for _ in range(counts[num]):
        print(num)
