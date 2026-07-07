'''-------------------------------------------
Sub : [BOJ] 홀짝홀짝
Link: https://www.acmicpc.net/problem/31867
Tag : Python, 구현, 문자열, 수학
Memo
-------------------------------------------'''

N = int(input())
K = input()

even = 0
odd = 0

for char in K:
    if int(char)%2 == 0:
        even += 1
    else:
        odd += 1

result = 0 if even>odd else (1 if odd>even else -1)
print(result)
