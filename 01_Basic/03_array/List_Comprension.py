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
    # 각 줄에서 R과 S를 분리
    R, S = input().split()
    R = int(R)
    
    # 문자열 P 생성 (list comprehension)
    P = ''.join([char * R for char in S])
    
    # 결과 출력
    print(P)
