'''
----------------------------------------------
Sub : [BOJ] OX퀴즈
Link: https://www.acmicpc.net/problem/8958
Tag : Python, 
Memo
----------------------------------------------
'''

# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    score = 0
    result = 0
    for i in input().strip():
        if i == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)
