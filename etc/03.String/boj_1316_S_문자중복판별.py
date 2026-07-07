'''---------------------------------------------
Sub  : [BOJ] 그룹 단어 체커
Link : https://www.acmicpc.net/problem/1316
Level: 실버 5
Tag  : Python, 문자열
Memo
 - 단어의 중복 문제는 set()을 사용하여 풀기
---------------------------------------------'''

import sys
input = sys.stdin.readline

N = int(input().strip())
count = 0

for _ in range(N):
    chars = input().strip()
    seen = set()
    prev_char = None
    is_group_word = True

    for char in chars:
        if char != prev_char:  # 문자가 바뀔 때
            if char in seen:   # 이미 등장했던 문자면 그룹 단어가 아님
                is_group_word = False
                break
            seen.add(char)
        prev_char = char

    if is_group_word:
        count += 1

print(count)
