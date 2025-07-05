'''
----------------------------------------------
Sub : [BOJ] 단어의 개수
Link: https://www.acmicpc.net/problem/1152
Tag : Python, string
Memo
----------------------------------------------
'''

def count_words(s):
    words = s.split()  # 공백을 기준으로 단어를 분리
    return len(words)  # 단어의 개수를 반환


s = input().strip()  # 입력받은 문자열의 양 끝 공백을 제거

# 단어의 개수를 출력
print(count_words(s))
