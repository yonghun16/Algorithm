'''
----------------------------------------------
Sub : [BOJ] 숫자의 개수
Link: https://www.acmicpc.net/problem/2577
Tag : Python, 
Memo
----------------------------------------------
'''

# 입력 받기
A = int(input())
B = int(input())
C = int(input())

# A × B × C의 결과 계산
result = A * B * C

# 결과를 문자열로 변환
result_str = str(result)

# 0부터 9까지 각 숫자의 빈도 계산 및 출력
for i in range(10):
    count = result_str.count(str(i))
    print(count)
