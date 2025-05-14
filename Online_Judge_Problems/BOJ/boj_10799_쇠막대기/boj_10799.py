'''----------------------------------------------------
Sub  : [BOJ] 쇠막대기2
Link : https://www.acmicpc.net/problem/10799
Level: 실버 2
Tag  : Python, Stack
Memo
 - 쇠막대기 기준으로 쪼갠다.
 - 규칙을 발견한다.
    - '('를 만날 때마다 스택에 '('를 추가한다.(쇠막대기의 개수를 추가)
    - 스택의 최상단이 '('이고. ')'를 만난다면 스택의 크기만큼 총 개수에 추가한다.(체이저를 발사하면 현재 쇠막대기의 개수만큼 총 개수가 증가한다.)
    - ')'를 만난다면 총 개수에 1을 추가한다.(쇠막대기가 종료되면 총 개수는 1이 증가하기 때문)
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 변수
input_data = input().strip()            # 괄호 문자의 개수는 최대 100,000

# 출력 변수
answer = 0

# 풀이
stack = []

for i in range(len(input_data)):        # 괄호의 개수만큼 반복
    if input_data[i] == '(':            # 괄호이면 -> 새로운 쇠막대기 시작
        stack.append(input_data[i])     # 스택에 현재 데이터를 입력
    else:
        if input_data[i-1] == '(':      # 그렇지 않으면(현재 ')'이면), 그리고 이전에 '('이면 -> 새로운 레이저 시작
            stack.pop()                 # 스택의 최종 데이터를 제거
            answer += len(stack)        # 누적된 스택의 크기를 answer에 더함
        else:
            stack.pop()                 # 스택의 최종 데이터를 제거
            answer += 1                 # 정답에 1을 더함.


# 출력
print(answer)
