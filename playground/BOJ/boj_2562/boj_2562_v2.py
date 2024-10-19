'''
----------------------------------------------
Sub : [BOJ] 최댓값
Link: https://www.acmicpc.net/problem/2562
Tag : Python, Math
Memo
----------------------------------------------
'''

numbers = []

# 9개의 숫자를 입력받음
for _ in range(9):
    num = int(input())
    numbers.append(num)

max_value = max(numbers)
max_index = numbers.index(max_value) + 1

# 출력
print(max_value)
print(max_index)
