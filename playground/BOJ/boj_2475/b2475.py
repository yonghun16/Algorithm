# 검증수
# https://www.acmicpc.net/problem/2475

# 검증수를 구하는 함수
def getVerification(a, b, c, d, e):
    return (a * a + b * b + c * c + d * d + e * e) % 10

# 사용자 입력을 받음
numbers = input().split()
a, b, c, d, e = map(int, numbers)
answer = getVerification(a, b, c, d, e)
print(answer)
