'''---------------------------------------------
Sub  : [BOJ] 피보나치 수 5
Link : https://www.acmicpc.net/problem/10870
Level: Bronze 2
Tag  : Python, 피보나치, 동적계획
Memo
 - 
---------------------------------------------'''

import sys
input = sys.stdin.readline

n = int(input().strip())

a, b = 0, 0

for i in range(n):
    if(i==0):
        a, b = 0, 1
        continue
    a, b = b ,a+b

print(b)
