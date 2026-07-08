# https://www.acmicpc.net/problem/1002
import math

t = int(input())
while(True):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distanse = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if(r1>r2): subtract = r1-r2
    else: subtract = r2-r1
    if(distanse == 0 and r1 == r2): result = -1 # 두 원이 완전히 일치하는 경우
    elif(distanse < r1 + r2 and (subtract < distanse)): result = 2  # 두 원의 교점이 2개일 경우
    elif(distanse == r1 + r2 or distanse == subtract): result = 1  # 두 원의 교점이 1개일 경우
    else: result = 0  # 두 원의 교점이 없을 경우
    print(result)
    t = t-1
    if(t == 0): break
