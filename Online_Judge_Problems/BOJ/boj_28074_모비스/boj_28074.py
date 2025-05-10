'''----------------------------------------------------
Sub  : [BOJ] 
Sub : [BOJ] 모비스
Link : https://www.acmicpc.net/problem/
Link: https://www.acmicpc.net/problem/28074
Level: 브론즈 4
Tag  : Python, String
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

def can_form_mobis(string):
    required_chars = "MOBIS"

    for char in required_chars:
        if string.count(char) < 1:
            return "NO"
    return "YES"

input_string = input().strip()

# 결과 출력
print(can_form_mobis(input_string))
