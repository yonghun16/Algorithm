# 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3003

pieces_of_right = [1, 1, 2, 2, 2, 8]

pieces_of_input = list(map(int, input().split()))

results = []

for i in range(6):
    results.append(pieces_of_right[i] - pieces_of_input[i])

print(" ".join(map(str, results)))
