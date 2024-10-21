'''
----------------------------------------------
Sub : [BOJ] ACM호텔
Link: https://www.acmicpc.net/problem/10250
Tag : Python
Memo
----------------------------------------------
'''
 
T = int(input())

def sol(H, W, N):
    rows = W
    cols = H
    number = 1;
    for i in range(W):
        for j in range(H):
            if number == N:
                print((j+1)*100 + (i+1))
            number += 1


for _ in range(T):
    H, W, N = map(int, input().split())
    sol (H, W, N)



