# AxB -7
# https://www.acmicpc.net/problem/11021

t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split())

    print(f"Case #{i}: {a + b}")