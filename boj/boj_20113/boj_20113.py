'''---------------------------------------------
Sub  : [BOJ] 긴급 회의
Link : https://www.acmicpc.net/problem/20113
Level: B1
Tag  : Python, 구현
Memo
 - 
---------------------------------------------'''

import sys
input = sys.stdin.readline

N = int(input().strip())
X = list(map(int,input().split()))

votes = [0 for _ in range(N)]
max_vote = 0
imposter = 0
count = 0

# 가장 많이 받은 투표수(max_vote)와 그 사람(imposter)을 검색
for i in range(N):
    if(int(X[i]) != 0):
        votes[int(X[i])-1] += 1
        if max_vote < votes[int(X[i])-1]:
            max_vote = votes[int(X[i])-1]
            imposter = X[i]

# 가장 많이 받은 투표 수 중복수를(count) 체크
for vote in votes:
    if vote == max_vote:
        count += 1
    
# 결과 출력
if count > 1:
    print("skipped")
else:
    print(imposter)
