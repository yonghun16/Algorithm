'''---------------------------------------------
Sub  : [BOJ] 카드 역배치
Link : https://www.acmicpc.net/problem/10804
Level: B2
Tag  : Python, 구현
Memo
 - 슬라이싱
---------------------------------------------'''

import sys
input = sys.stdin.readline

# 1부터 20까지의 카드 배열 초기화
cards = list(range(1, 21))

# 10개의 구간을 입력받아 뒤집기
for _ in range(10):
    a, b = map(int, input().split())
    # 1-based index를 0-based index로 변환
    cards[a-1:b] = cards[a-1:b][::-1]

# 결과 출력
print(*cards)
