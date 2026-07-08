'''
----------------------------------------------
Sub : [BOJ] Since 1973
Link: https://www.acmicpc.net/problem/28135
Tag : Python, 
Memo
----------------------------------------------
'''

n = int(input())
result = 0
num = 0
flag = 0

for i in range(1, n+1):
    if flag == 1:
        result += 1
        flag = 0

    result += 1
    num = str(i)
    num_len = len(num)
    for j in range(0, num_len-1):
        if (num[j] == '5' and num[j+1] == '0'):
            flag = 1
            break

print(result)
