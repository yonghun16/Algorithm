'''
----------------------------------------------
Sub : [BOJ] 문자열 반복
Link: https://www.acmicpc.net/problem/2675
Tag : Python, 
Memo
----------------------------------------------
'''

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    S = input()     # 문자열 입력
                    # 각 줄에서 R과 S를 분리
    R = int(S[0])   # 문자를 반복할 수 R 
    S = S[2:]       # S에서 문자열만 추출

    # 결과 출력
    for i in S:
        print(i*R, end="")
    print()

