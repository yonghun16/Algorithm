# 주사위 세개
# https://www.acmicpc.net/problem/2480

a, b, c = map(int, input().split())

if a==b and b==c:
    print(a*1000 + 10000)
elif a==b: 
    print(a*100 + 1000)
elif a==c:
    print(a*100 + 1000);
elif b==c:
    print(b*100 + 1000);
else:
    print(max(a,b,c)*100)
