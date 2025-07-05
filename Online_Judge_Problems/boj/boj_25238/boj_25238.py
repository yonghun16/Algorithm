'''----------------------------------------------------
Sub  : [BOJ] 가희와 방어율 무시
Link : https://www.acmicpc.net/problem/25238
Level: 브론즈 4
Tag  : Python, 사칙연산
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

def get_effective_defence(a, b):
    return int(a * (100-b)/100)

# 입력 받기
# (a -> 몬스터 방어율 수치, b -> 유저의 방무)
a, b = map(int, input().strip().split())

effective_defence = get_effective_defence(a, b)

# 출력 하기
if effective_defence >= 100:
    print(0)
else:
    print(1)

