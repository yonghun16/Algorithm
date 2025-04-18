'''
----------------------------------------------
Sub : [BOJ] 
Link: https://www.acmicpc.net/problem/4388
Tag : Python, 
Memo
----------------------------------------------
'''

def carry(n, m):
    one_place = len(n) if len(n)>len(m) else len(m)
    count = 0
    carry_number = 0

    for i in range(one_place-1, -1, -1):
        if int(n[i]) + int(m[i]) + carry_number >=10:
            count += 1
            carry_number = 1
        else:
            carry_number = 0
        
    return(count)

while True:
    n, m = input().split()
    if n=='0' and m=='0':
        break
    n = list(n)
    m = list(m)

    if len(n) > len(m):
        for i in range(len(n)-len(m)):
            m = ['0', *m]
    elif len(n) < len(m):
        for i in range(len(m)-len(n)):
            n = ['0', *n]

    print(carry(n, m))

