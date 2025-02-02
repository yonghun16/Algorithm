'''----------------------------------------------------
Sub  : [BOJ] 팰린드롬수
Link : https://www.acmicpc.net/problem/1259
Level: 브론즈 1
Tag  : Python, String
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

while True:
    # 입력
    n = input().strip()

    if n == '0':
        break;

    # 출력
    if n == n[::-1]:
        print('yes')
    else :
        print('no')
