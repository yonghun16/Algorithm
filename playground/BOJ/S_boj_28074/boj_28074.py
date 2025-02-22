'''
----------------------------------------------
Sub : [BOJ] 모비스
Link: https://www.acmicpc.net/problem/28074
Tag : Python, String
Memo
----------------------------------------------
'''

def can_form_mobis(string):
    required_chars = "MOBIS"

    for char in required_chars:
        if string.count(char) < 1:
            return "NO"
    return "YES"

input_string = input().strip()

# 결과 출력
print(can_form_mobis(input_string))
