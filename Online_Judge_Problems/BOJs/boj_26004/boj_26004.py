'''---------------------------------------------
Sub  : [BOJ] HI-ARC
Link : https://www.acmicpc.net/problem/26004
Level: B3
Tag  : Python, 구현, 문자열
Memo
 - 굳이 딕셔너리를 쓸 필요는 없다.
---------------------------------------------'''

import sys
input = sys.stdin.readline

N = int(input().strip())
S = input().strip()

hiarc = {
    'H': 0,
    'I': 0,
    'A': 0,
    'R': 0,
    'C': 0
}

for ch in S:
    if ch == 'H' : hiarc['H'] += 1
    elif ch == 'I' : hiarc['I'] += 1
    elif ch == 'A' : hiarc['A'] += 1
    elif ch == 'R' : hiarc['R'] += 1
    elif ch == 'C' : hiarc['C'] += 1

ch_min = min(hiarc['H'], hiarc['I'], hiarc['A'], hiarc['R'], hiarc['C'])

print(ch_min)
