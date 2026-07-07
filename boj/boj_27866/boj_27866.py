'''
----------------------------------------------
Sub: [BOJ] 27866. 문자와 문자열
Link: https://www.acmicpc.net/problem/27866
Tag: python, 문자열
Memo
- 문자열은 0부터 인덱스 시작
----------------------------------------------
'''

# 문자열 S와 정수 i입력 받기
S = input().strip()
i = int(input())

# 결과 출력
print(S[i-1])
