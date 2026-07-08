"""
-----------------------------------------------------------
Sub    : [BOJ] 임시 반정 정하기
Link   : https://www.acmicpc.net/problem/1268
Level  : 실버 5
Tag    : Python, 구현
-----------------------------------------------------------
Details

-----------------------------------------------------------
"""

import os
import sys

if sys.platform == "linux":
    lines = sys.stdin.read().strip().split("\n")
else:
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")

input = iter(lines).__next__

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

max_count = -1
leader = 0

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        # 1~5학년 중 같은 반이 있었는지 확인
        for year in range(5):
            if classes[i][year] == classes[j][year]:
                count += 1
                break
    # 최댓값 갱신 (동점이면 번호 작은 쪽 유지)
    if count > max_count:
        max_count = count
        leader = i + 1  # 학생 번호는 1부터

print(leader)
