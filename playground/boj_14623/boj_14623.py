'''
----------------------------------------------
Sub : [BOJ] 
Link: https://www.acmicpc.net/problem/14623
Tag : Python, 
Memo
----------------------------------------------
'''

# input
b1 = input()
b2 = input()

result = int(b1, 2) * int(b2, 2)

# print result
print(bin(result)[2:])
