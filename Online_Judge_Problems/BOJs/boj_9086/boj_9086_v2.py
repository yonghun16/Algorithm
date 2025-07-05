'''
----------------------------------------------
Sub : [BOJ] 문자열
Link: https://www.acmicpc.net/problem/9086
Tag : Python, 문자열
Memo
----------------------------------------------
'''

# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    s = input()
    # 첫 글자와 마지막 글자를 추출하여 출력
    print(s[0] + s[-1])
