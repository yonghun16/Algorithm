'''
----------------------------------------------
Sub : [BOJ] 모음의 개수
Link: https://www.acmicpc.net/problem/1264
Tag : Python, 
Memo
----------------------------------------------
'''

def count_vowels(line):
    vowels = "aeiouAEIOU"
    count = 0
    for char in line:
        if char in vowels:
            count += 1
    return count

while True:
    line = input().strip()
    if line == '#':
        break
    print(count_vowels(line))
