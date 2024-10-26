'''
----------------------------------------------
Sub : [BOJ] ACM호텔
Link: https://www.acmicpc.net/problem/10250
Tag : Python
Memo
----------------------------------------------
'''
 
T = int(input())  # 테스트 케이스 개수 입력

def sol(H, W, N):
    number = 1;
    for i in range(W):
        for j in range(H):
            if number == N:
                print((j+1)*100 + (i+1))
            number += 1


for _ in range(T):
    H, W, N = map(int, input().split())  # 호텔의 층 수, 각 층의 방 수, N번째 손님
    sol (H, W, N)

