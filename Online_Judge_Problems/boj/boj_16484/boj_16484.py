'''-------------------------------------------
Sub : [BOJ] 접시 안의 원
Link: https://www.acmicpc.net/problem/16483
Tag : Python, 기하학
Memo
-------------------------------------------'''

T = int(input())

result = (T ** 2) / 4

# 소수 첫째 자리에서 반올림하여 출력
print(round(result))
