# 오븐 시계
# https://www.acmicpc.net/problem/2525

a, b = map(int, input().split())
c = int(input())

totalMinute = a*60 + b + c   # 분의 형태로 바꾸기
totalMinute %= 1440  # 24*60=1440
a = int(totalMinute/60)
b = totalMinute % 60

print(a, b)
