'''---------------------------------------------
Sub  : [BOJ] 블랙잭
Link : https://www.acmicpc.net/problem/2798
Level: Bronze 2 
Tag  : Python, 브루트포스
Memo
 - 
---------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

def blackjack(N, M, cards):
    max_sum = 0

    # 3중 for문으로 카드 3장을 선택
    for i in range(N-2):
        for j in range(i + 1, N-1):
            for k in range(j + 1, N):
                current_sum = cards[i] + cards[j] + cards[k]
                if current_sum <= M:
                    max_sum = max(max_sum, current_sum)
    
    return max_sum

# 결과 출력
print(blackjack(N, M, cards))
