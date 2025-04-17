'''----------------------------------------------------
Sub  : [BOJ] 거꾸로 구구단
Link : https://www.acmicpc.net/problem/13410
Level: 브론즈 2
Tag  : Python, 구현
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())   # 입력 값
answer = 0                                 # 출력 값


# 변수 선언
maxNumber = 0    # 최대 값

# 구구단 숫자를 거꾸로 구하기
def reverseTimesTable(str):
    resultNumber = []
    for i in range(len(str)-1, -1, -1):
        resultNumber.append(str[i])
    return int(''.join(resultNumber))


# 가장 큰 구구단 수 구하기
for _ in range(2, K+1):
    currentNumber = reverseTimesTable(str(N * _))

    if (maxNumber < currentNumber):
        maxNumber = currentNumber

    answer = maxNumber


# 결과 출력
print(answer)
