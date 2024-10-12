'''
----------------------------------------------
Sub : [BOJ] 이상한 기호
Link: https://www.acmicpc.net/problem/15964
Tag : python, 문자열
Memo
----------------------------------------------
'''

# (A+B)*(A-B)결과를 리턴하는 함수
def solution(A, B):
    return (A+B)*(A-B)

A, B = input().split()

# (A+B)*(A-B)의 값를 출력
print(solution(int(A), int(B)))
