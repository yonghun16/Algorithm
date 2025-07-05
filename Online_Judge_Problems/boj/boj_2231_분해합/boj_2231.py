'''
----------------------------------------------
Sub : [BOJ] 분해합
Link: https://www.acmicpc.net/problem/2231
Tag : Python, 
Memo
----------------------------------------------
'''

N = int(input())
cnt = N
minN = N

# 생성자를 반환하는 함수
def devideSum(num):
    el = str(num)
    elSum = num

    for _ in el:
        elSum += int(_)

    if elSum == N:
        return num
    
    return 0


while cnt > N/2:
    cnt -= 1
    cur = devideSum(cnt)
    
    if cur != 0 and cur < minN :
        minN = cur

# 출력
if minN == N:
    print(0)
else :
    print(minN)


