'''
----------------------------------------------
Sub : [BOJ] 파일 옮기기
Link: https://www.acmicpc.net/problem/11943
Tag : Python, 
Memo
----------------------------------------------
'''

a, b = map(int, input().split())
c, d = map(int, input().split())

if (b+c < a+d):
    result = b+c
else :
    result = a+d

print(result)
