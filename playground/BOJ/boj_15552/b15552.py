# 빠른 A+B
# https://www.acmicpc.net/problem/15552

import sys
caseCount = int(input())

for _ in range(caseCount):
    firstNumber, secondNumber = map(int, sys.stdin.readline().split())
    print(firstNumber + secondNumber)
