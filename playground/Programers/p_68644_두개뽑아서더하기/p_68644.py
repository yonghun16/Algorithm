'''----------------------------------------------------
Sub  : [Programmers] 두 개 뽑아서 더하기
Link : https://school.programmers.co.kr/learn/courses/30/lessons/68644
Level: 1
Tag  : Python, 
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

def solution(numbers):
    temp = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp.append(numbers[i] + numbers[j])

    answer = list(set(temp))
    answer.sort()

    return answer
