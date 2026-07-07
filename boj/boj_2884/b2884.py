# 알람 시계
# https://www.acmicpc.net/problem/2884

h, m = map(int, input().split())

if (m < 45):
    h -= 1;
    m += 15;
    if h < 0: h = 23
else: m -= 45

print(h, m)
