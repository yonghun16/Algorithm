'''
----------------------------------------------
Sub : [BOJ] 알파벳 찾기
Link: https://www.acmicpc.net/problem/10809
Tag : Python, String
Memo
----------------------------------------------
'''

s = input()

for i in range(97, 123):
    print(s.find(chr(i)), end=' ')
