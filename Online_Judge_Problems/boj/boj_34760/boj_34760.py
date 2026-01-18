import sys

# 15마리 코끼리의 코 길이를 입력받음
a = list(map(int, sys.stdin.readline().split()))

# 1. 앞의 14마리는 무조건 기절해야 함 (당근 > 코 길이)
# 즉, 앞 14마리의 최댓값보다 최소 1은 커야 함
max_front = max(a[:14]) + 1

# 2. 마지막 15번째 코끼리는 잠들어도 됨 (당근 >= 코 길이)
# 즉, 마지막 코끼리의 코 길이보다 크거나 같으면 됨
last_elephant = a[14]

# 두 조건 중 더 큰 값이 모든 코끼리를 멈추는 최소 당근 길이
print(max(max_front, last_elephant))
