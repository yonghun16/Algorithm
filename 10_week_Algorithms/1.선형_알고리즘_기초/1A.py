# 문제1A 최대값 함수

# a, b 중 최대값을 반환하는 함수
def getMax(a, b):
    if a>b:
        return a
    else:
        return b

a, b = map(int, input().split())
print(getMax(a, b))
