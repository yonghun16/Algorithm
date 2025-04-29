'''----------------------------------------------------
Sub  : [BOJ] 369
Link : https://www.acmicpc.net/problem/17614
Level: 브론즈 3
Tag  : Python, 브루투포스
Memo
----------------------------------------------------'''

import sys
input = sys.stdin.readline

# 입력 변수
N = int(input().strip())

# 출력 변수
answer = 0

# 369 박수 수 구하기
# 시간복잡도 : O(N^2)
clap_count = 0
for i in range(1, N + 1):
    str_i = str(i)
    clap_count += str_i.count('3') + str_i.count('6') + str_i.count('9')


# 출력
answer = clap_count
print(answer)
