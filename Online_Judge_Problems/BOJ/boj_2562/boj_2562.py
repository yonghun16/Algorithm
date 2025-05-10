'''
----------------------------------------------
Sub : [BOJ] 최댓값
Link: https://www.acmicpc.net/problem/2562
Tag : Python, Math
Memo
----------------------------------------------
'''

max_value = 0
max_index = 0

# 9개의 숫자를 입력받음
for _ in range(9):
    num = int(input())
    if num > max_value:
        max_value = num
        max_index = _ + 1

# 출력
print(max_value)
print(max_index)
