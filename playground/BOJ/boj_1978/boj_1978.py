'''
----------------------------------------------
Sub : [BOJ] 소수 찾기
Link: https://www.acmicpc.net/problem/1978
Tag : Python, Math
Memo
----------------------------------------------
'''

def isPrimeNumber(num):
    if num <= 1:
        return 0
    elif num % 2 == 0 and num != 2:
        return 0
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return 0
    return 1


count = 0

n = int(input())
inputDataList = [int(w) for w in input().split()]

for w in inputDataList:
    count += isPrimeNumber(w)

print(count)



