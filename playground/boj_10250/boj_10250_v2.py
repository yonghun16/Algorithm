'''
----------------------------------------------
Sub : [BOJ] ACM호텔
Link: https://www.acmicpc.net/problem/10250
Tag : Python
Memo
----------------------------------------------
'''
 
T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    H, W, N = map(int, input().split())  # 호텔의 층 수, 각 층의 방 수, N번째 손님
    
    # 손님이 배정될 층 수 (층 번호는 1부터 시작하므로 나머지가 0일 경우 H층)
    floor = N % H
    if floor == 0:
        floor = H
    
    # 손님이 배정될 방 번호 (1부터 시작, 나머지가 0일 경우 한 층 위로)
    room = (N - 1) // H + 1
    
    # 방 번호를 출력 (층 수와 방 번호를 2자리로)
    print(f"{floor}{room:02d}")
