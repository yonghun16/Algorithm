'''----------------------------------------------------
Sub  : [BOJ] 스택 수열
Link : https://www.acmicpc.net/problem/1874
Level: 실버 2
Tag  : Python, Stack
Memo
----------------------------------------------------'''

import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for num in sequence:
    # 원하는 숫자까지 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 top 확인
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")
