'''----------------------------------------------------
Sub : [BOJ] Caesar Cipher
Link: https://www.acmicpc.net/problem/15874
Level: 브론즈 2
Tag  : Python, math 
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline


import sys
input = sys.stdin.readline

def caesar_cipher(k, s):
    k = k % 26  # k가 26 이상일 경우를 대비해서, 26으로 나눈 나머지로 축소
    result = []

    for char in s:
        if 'A' <= char <= 'Z':  # 대문자
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
            result.append(new_char)
        elif 'a' <= char <= 'z':  # 소문자
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            result.append(new_char)
        else:
            # 공백, 온점, 쉼표는 그대로 출력
            result.append(char)

    return ''.join(result)

# 입력 받기
k, n = map(int, input().split())
s = input()

# 암호화된 문자열 출력
print(caesar_cipher(k, s))
