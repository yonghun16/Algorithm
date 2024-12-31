'''
----------------------------------------------
Sub : [BOJ] 체육은 코딩과목 입니다.
Link: https://www.acmicpc.net/problem/28295
Tag : Python, 
Memo
----------------------------------------------
'''

result = 0

for _ in range(10):
    n = int(input())
    result += n
    if result > 3:
        result -= 4

if result == 0:
    result = 'N'
elif result == 1:
    result = 'E'
elif result == 2:
    result = 'S'
else :
    result = 'W'

print(result)
