'''---------------------------------------------
Sub  : [BOJ] Hashing
Link : https://www.acmicpc.net/problem/15829
Level: 브론즈 2
Tag  : Python, 구현, 문자열, 해싱
Memo
 - ord() 문자를 유니 코드로 변환
---------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 받기
L = int(input())
string = input()

# 해시 함수의 r과 M 값 설정
r = 31
M = 1234567891

# 해시 값 계산
hash_value = 0
for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1  # 알파벳의 고유 번호 (a=1, b=2, ..., z=26)
    hash_value += char_value * (r ** i)
    hash_value %= M

# 결과 출력
print(hash_value)
