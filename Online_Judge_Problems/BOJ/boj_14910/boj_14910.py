'''
----------------------------------------------
Sub : [BOJ] 오르막
Link: https://www.acmicpc.net/problem/14910
Tag : Python, 
Memo
----------------------------------------------
'''

numbers = list(map(int, input().split()))

result = "Good"

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        result = "Bad"

print(result)
