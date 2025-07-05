'''
----------------------------------------------
Sub : [BOJ] 16진수
Link: https://www.acmicpc.net/problem/1550
Tag : Python, Math
Memo
----------------------------------------------
'''

N = input()
power = 0
DexNum = 0
sumNum = 0

for i in range(len(N)-1, -1, -1):
    if N[i] == 'A':
        DexNum = 10
    elif N[i] == 'B':
        DexNum = 11
    elif N[i] == 'C':
        DexNum = 12
    elif N[i] == 'D':
        DexNum = 13
    elif N[i] == 'E':
        DexNum = 14
    elif N[i] == 'F':
        DexNum = 15
    else:
        DexNum = int(N[i])

    sumNum += DexNum*(16**power)
    power += 1

print(sumNum)
